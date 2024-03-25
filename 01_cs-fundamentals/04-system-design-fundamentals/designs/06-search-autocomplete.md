# Design 06: Search Autocomplete

## Requirements
- **Functional requirements**:
  - As a user types, provide a list of top-k suggestions.
  - Suggestions should be based on search popularity (frequency).
  - Support real-time updates (or near real-time) of the suggestion list.
- **Non-functional requirements**:
  - **Ultra-low Latency**: Suggestions must appear within 100ms of typing.
  - **High Availability**: The system must remain available even if some nodes fail.
  - **Scalability**: Support 100M Daily Active Users and 1B searches per day.

## Capacity Estimation
- **Traffic**: 1B searches per day.
- **Query Load**: 100M DAU * 10 searches/user/day = 1B searches.
- **Average Chars/Search**: 20 chars. Each character typed is a request.
- **Requests per Second (RPS)**: (1B * 20) / 86,400 ≈ 231,000 RPS (Average).
- **Peak RPS**: 231,000 * 2 = 462,000 RPS.
- **Trie Size**: Assuming 100M unique search terms, each term avg 10 bytes = 1 GB. Including frequencies and child nodes, the Trie can fit in memory (~10-20 GB).

## High-Level Architecture
```
[User] -> [Load Balancer] -> [Autocomplete Service]
                                | (Read Trie from RAM)
                   +------------+------------+
                   |                         |
           [Analytics Service]       [Trie Builder (Offline)]
                   |                         |
           [Frequency DB (NoSQL)] <------> [Trie DB (S3/HDFS)]
```
- **Autocomplete Service**: Fast, in-memory service that serves top-k suggestions.
- **Analytics Service**: Captures real-time search events and updates frequencies.
- **Trie Builder**: Periodic (hourly/daily) process that builds the Trie from the Frequency DB.
- **Trie DB**: Persistent storage for the serialized Trie structure.

## Data Model
- **Trie Structure**:
  - `node`: { `is_end`: bool, `frequency`: int, `top_k`: list[string], `children`: dict[char, node] }
- **Frequency DB (NoSQL)**:
  - `query` (PK), `frequency` (Counter).
- **Why this schema**: Storing the `top_k` results directly at each node in the Trie allows for $O(L)$ lookup (L = length of prefix) instead of $O(L + N \log K)$.

## Key Design Decisions
1. **Pre-calculating Top-K**: Instead of traversing all children of a prefix at query time, pre-calculate the top-k most popular searches at each node. This makes the search constant time regardless of the number of children.
2. **Offline vs. Online Trie Update**: Chose **Offline Trie Building** for better performance. Real-time updates to a complex Trie are slow and can cause concurrency issues. Near real-time is sufficient for autocomplete.
3. **In-Memory Serving**: The entire Trie is loaded into the RAM of the Autocomplete Service for sub-10ms response times.

## Bottlenecks & How to Scale
1. **Trie Size**: If the number of unique searches grows too large for one server's RAM, **Shard the Trie** by prefix (e.g., shard A-G, shard H-M, etc.).
2. **High Write Throughput (Analytics)**: 231k RPS for analytics is heavy. Use **Kafka** to buffer search events and update the Frequency DB asynchronously in batches.
3. **Browser Latency**: Even with 10ms server time, network latency can be >100ms. Use **Browser Caching** (cache the results of the first 2-3 characters) to reduce redundant requests.

## What I Would Do Differently at 10x Scale
- **Sampling**: Instead of tracking 100% of searches in the Analytics Service, track 1% or 10% to reduce the load on the Frequency DB.
- **Edge Serving**: Use **Edge Computing** (e.g., Cloudflare Workers) to serve the Trie from points of presence closer to the user.
- **Personalization**: Incorporate user history and location into the top-k ranking (e.g., "piz..." suggests "pizza near me" if location is enabled).

# Design 01: URL Shortener

## Requirements
- **Functional requirements**:
  - Shorten a long URL to a unique short code.
  - Redirect users from the short code to the original long URL.
  - Custom short aliases.
  - Expiration of links.
- **Non-functional requirements**:
  - High availability (100M URLs).
  - Low latency (<10ms reads).
  - Scalability to handle high traffic.

## Capacity Estimation
- **DAU**: 1M users.
- **Read/Write Ratio**: 100:1 (Heavy read).
- **Writes per second**: 1M / 86400 ≈ 12 writes/sec.
- **Reads per second**: 100 * 12 = 1200 reads/sec.
- **Storage (10 years)**: 100M URLs/year * 10 years * 500 bytes/URL ≈ 500 GB.
- **Cache**: 20% of daily reads (120M * 0.2 * 500 bytes) ≈ 12 GB RAM.

## High-Level Architecture
```
[User] -> [Load Balancer] -> [API Service] -> [Cache (Redis)]
                                    |
                                    v
                            [Database (NoSQL/SQL)]
```
- **Load Balancer**: Distribute traffic.
- **API Service**: Handle logic and redirections.
- **Cache**: Store hot URLs for sub-10ms reads.
- **Database**: Persistent storage of URL mappings.

## Data Model
- **Table: `urls`**
  - `short_id` (PK, string, indexed): The short code.
  - `long_url` (string): The original URL.
  - `created_at` (datetime)
  - `expires_at` (datetime)

## Key Design Decisions
1. **Hashing vs. Base62 Encoding**: Chose Base62 encoding of a unique ID (from a Snowflake-like service) to avoid collisions and ensure fixed length.
2. **SQL vs. NoSQL**: Chose NoSQL (Cassandra/DynamoDB) for high availability and easy scaling as the workload is mostly K-V lookups.
3. **Caching Strategy**: Cache-aside with LRU eviction to keep hot links in memory for latency targets.

## Bottlenecks & How to Scale
1. **Database Write Throughput**: Use a distributed ID generator to prevent bottlenecks at the DB insertion point.
2. **Global Latency**: Use a CDN or Geo-distributed caches/DB replicas.
3. **Cache Invalidation**: Use TTLs and LRU to keep the cache fresh and manageable.

## What I Would Do Differently at 10x Scale
- Use a globally distributed multi-master database.
- Implement more aggressive rate limiting at the edge.
- Use regional load balancing to route users to the nearest data center.

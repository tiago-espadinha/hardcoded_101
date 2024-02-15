# Design 02: Twitter Feed

## Requirements
- **Functional requirements**:
  - Tweet creation.
  - Home timeline (feed from followed users).
  - Following/Unfollowing users.
- **Non-functional requirements**:
  - High availability for 500M DAU.
  - Low latency for feed loading (<200ms).
  - Eventual consistency is acceptable for feed updates.

## Capacity Estimation
- **DAU**: 500M.
- **Tweets per day**: 500M * 2 tweets/day = 1B tweets/day.
- **Writes/sec**: 1B / 86400 ≈ 12k writes/sec.
- **Reads/sec (Feed loading)**: 500M * 10 feed loads/day / 86400 ≈ 60k reads/sec.
- **Storage per year**: 1B tweets * 200 bytes ≈ 200 GB/day ≈ 73 TB/year.

## High-Level Architecture
```
[User] -> [LB] -> [Tweet Service] -> [Write DB]
          |
          v
       [Feed Service] <- [Feed Cache (Redis)]
          |
          v
       [Fanout Service] -> [Message Queue]
```
- **Tweet Service**: Handles tweet creation and storage.
- **Fanout Service**: Pushes new tweets to followers' pre-computed feed caches.
- **Feed Service**: Serves the home timeline from the pre-computed cache.

## Data Model
- **Tweets**: `tweet_id` (PK), `user_id`, `content`, `timestamp`.
- **Follows**: `follower_id`, `followee_id` (Composite PK).
- **Feed Cache**: List of `tweet_ids` for each `user_id` in Redis.

## Key Design Decisions
1. **Push vs. Pull Model**: Hybrid approach. Push (Fanout) for regular users, Pull (On-demand) for celebrities to avoid "thundering herd" issues in Redis.
2. **SQL vs. NoSQL**: NoSQL (Cassandra) for tweets due to high write volume and time-series nature.
3. **Caching Strategy**: In-memory pre-computed feeds (Redis) to meet the 200ms latency requirement.

## Bottlenecks & How to Scale
1. **Celebrity Fanout**: Avoid pushing to millions of followers; instead, merge celebrity tweets during read-time.
2. **Redis Memory Limits**: Shard Redis by `user_id` and limit the number of tweets cached per user (e.g., top 1000).
3. **Read Latency**: Use CDNs for media content and edge caching for static components.

## What I Would Do Differently at 10x Scale
- Implement more complex feed ranking (ML-based) using dedicated ranking services.
- Use a custom storage engine optimized for append-only time-series data.
- Further regionalize data centers to reduce cross-region traffic.

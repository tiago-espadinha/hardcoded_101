# Design 04: Distributed Rate Limiter

## Requirements
- **Functional requirements**:
  - Limit the number of requests a user/IP can make in a given time period.
  - Support multiple rate-limiting algorithms (Token Bucket, Sliding Window Counter).
  - Provide a clear response (HTTP 429) when the limit is exceeded.
- **Non-functional requirements**:
  - **Low Latency**: The rate limiter must not add more than 5ms overhead per request.
  - **High Availability**: If the rate limiter service is down, the system should fail-open (allow requests) to avoid blocking users.
  - **Distributed**: Must work across multiple API servers and data centers.
  - **Scalability**: Handle 1 billion requests per day.

## Capacity Estimation
- **Traffic**: 1B requests per day.
- **Average RPS**: 1B / 86,400 ≈ 12,000 requests/sec.
- **Peak RPS**: 12,000 * 2 = 24,000 requests/sec.
- **Storage**: Assuming 100 million unique users/IPs. Each Redis entry (key + counter) takes ~50 bytes.
- **Memory**: 100M * 50 bytes = 5 GB. Even with 10x more users, a single Redis cluster can easily handle this.

## High-Level Architecture
```
[User] -> [Load Balancer] -> [API Gateway/Middleware]
                                |
                   +------------+------------+
                   |                         |
            [Rate Limiter]           [Backend Service]
                   |
            [Redis Cluster]
```
- **Rate Limiter (Middleware/Service)**: A component that sits between the LB and Backend, checks Redis, and decides whether to allow or block.
- **Redis Cluster**: Stores counters and timestamps for rate limiting. Using Redis allows for atomic operations and low-latency lookups.

## Data Model
- **Redis Keys**:
  - `rl:{user_id}:{endpoint}` -> `integer (counter)` (for fixed window)
  - `rl:{user_id}:{endpoint}` -> `hash (tokens, last_refill_time)` (for token bucket)
  - `rl:{user_id}:{endpoint}` -> `sorted set (timestamps)` (for sliding window log)

## Key Design Decisions
1. **Middleware vs. Centralized Service**: Chose **Middleware (in API Gateway)** for lower latency. This avoids an extra network hop that a separate "Rate Limit Service" would require.
2. **Algorithm**: Chose **Sliding Window Counter** as the default. It avoids the "spikes at window edges" problem of Fixed Window and uses less memory than Sliding Window Log.
3. **Storage**: Chose **Redis** over local memory. While local memory is faster, it doesn't work for distributed systems where users hit multiple servers. Redis `INCR` and `EXPIRE` are atomic and efficient.

## Bottlenecks & How to Scale
1. **Redis Performance**: 24k RPS is well within a single Redis node's capacity, but to scale to 100k+, use **Redis Sharding** (Cluster Mode) based on `user_id`.
2. **Race Conditions**: Two requests from the same user arriving at the same time could lead to over-counting. Solve this using **Lua Scripts** in Redis to ensure the check-and-increment is one atomic operation.
3. **Global Latency**: For multi-region deployments, a single Redis cluster in US-East will cause high latency for users in Asia. Use **Regional Redis Clusters** and sync configuration globally, but keep counters local to the region.

## What I Would Do Differently at 10x Scale
- **Hybrid Rate Limiting**: Implement a 2-tier system. Tier 1: In-memory local rate limiting on each API server (very fast). Tier 2: Periodically sync local counters to a global Redis cluster (consistent).
- **Client-side Throttling**: Expose rate limit headers (X-RateLimit-Limit, X-RateLimit-Remaining) to encourage clients to back off before they are blocked.
- **Adaptive Rate Limiting**: Automatically lower the limits during system-wide outages or high backend latency to protect downstream services.

# Caching Strategies

Caching is a core technique for improving system performance by storing frequently accessed data in a fast, temporary storage layer (like Redis or Memcached).

## 1. Cache-Aside (Lazy Loading)
The application first checks the cache. If it's a hit, it returns the data. If it's a miss, it reads from the database, stores the result in the cache, and returns it.
- **Pros:** Robust to cache failures (app falls back to DB); flexible for different data types.
- **Cons:** Cache misses can be slow; data can become stale if not manually invalidated on write.
- **Use Case:** General-purpose, read-heavy workloads.

## 2. Write-Through
The application writes to the cache and the database simultaneously. The write is only considered successful when both succeed.
- **Pros:** Data in the cache is always up-to-date; simplifies application logic (no stale cache issues).
- **Cons:** Higher write latency; can populate the cache with data that is never read.
- **Use Case:** Systems where data consistency is critical.

## 3. Write-Behind (Write-Back)
The application writes only to the cache. The cache then asynchronously flushes the update to the database after a delay.
- **Pros:** Extremely low write latency; can batch multiple writes to the database.
- **Cons:** Risk of data loss if the cache node crashes before flushing to the DB; complex implementation.
- **Use Case:** High-throughput write workloads where eventual consistency is acceptable.

## 4. Refresh-Ahead
The cache automatically refreshes an entry before it expires, based on predicted future access patterns.
- **Pros:** Extremely low latency for predicted data; prevents the "thundering herd" problem when a hot key expires.
- **Cons:** Can be difficult to predict access patterns accurately; consumes extra resources if predictions are wrong.
- **Use Case:** Highly predictable, latency-sensitive applications.

---

## Cache Invalidation
The most difficult part of caching is ensuring that the cache is consistent with the source of truth (the database). Common strategies include:
- **TTL (Time To Live):** Automatically expire entries after a set period.
- **Explicit Invalidation:** Manually delete or update cache entries when the database is updated.
- **Write-Through/Write-Behind:** (Described above) ensure the cache stays synchronized.

## Common Pitfalls
- **Cache Penetration:** Requests for non-existent keys bypass the cache and hit the database every time. (Fix: cache empty results or use Bloom filters).
- **Cache Avalanche:** Many cache entries expire at the same time, overwhelming the database. (Fix: add random jitter to TTLs).
- **Thundering Herd:** Multiple processes try to update the cache for the same missed key simultaneously. (Fix: use distributed locks).

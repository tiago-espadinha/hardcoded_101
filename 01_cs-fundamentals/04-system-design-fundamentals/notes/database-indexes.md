# Database Indexes

Indexes are data structures used by databases to speed up data retrieval operations. Without an index, the database must perform a full table scan, which is O(N) where N is the number of rows.

## 1. B-Tree Index (The Default)
A B-Tree is a balanced tree data structure that maintains sorted data. It is the most common type of index used in relational databases (e.g., PostgreSQL, MySQL).
- **Complexity:** O(log N) for search, insert, and delete.
- **Why it's popular:** Supports both exact match searches (`=`) and range queries (`>`, `<`). Its multi-level structure is optimized for disk-based storage, minimizing disk I/O.
- **Use case:** General-purpose indexing on IDs, names, dates, etc.

## 2. Hash Index
A hash index uses a hash table to map keys directly to row locations.
- **Complexity:** O(1) on average for search.
- **Cons:** Does not support range queries (`>`, `<`) because the hash values are not sorted; prone to hash collisions.
- **Use case:** Equality searches (`=`) in memory-based storage systems (like Redis) or specialized scenarios in Postgres (with `HASH` type).

## 3. Composite (Multi-column) Index
An index built on multiple columns (e.g., `(user_id, timestamp)`).
- **Rule of Thumb:** The order of columns in the composite index matters. It follows the "left-prefix" rule. An index on `(A, B)` can be used for queries on `(A)` or `(A, B)`, but NOT for queries only on `(B)`.
- **Use case:** Filtering by user and then sorting by time.

## 4. Covering Index
An index that contains all the columns required by a specific query.
- **Why it's fast:** The database can satisfy the query entirely from the index itself, without ever having to "hop" to the actual table data (the heap). This is known as an "Index-Only Scan".
- **Use case:** Frequent queries that only need a subset of columns.

---

## When to avoid indexes?
- **Small tables:** A full table scan might be faster than reading the index and then hopping to the data.
- **High write volume:** Every insert/update/delete must also update the corresponding indexes, adding overhead.
- **Columns with low cardinality:** (e.g., a "gender" column with only two values). The index won't filter enough rows to be useful.

## Misconceptions
- **"Indexes make everything faster":** No, they slow down writes (INSERT, UPDATE, DELETE).
- **"Just index every column":** This leads to massive storage overhead and slow writes. You should index based on actual query patterns.
- **"An index always gets used":** Database query planners are smart; they might choose a sequential scan if the index is large and they estimate most of the table will be read anyway.

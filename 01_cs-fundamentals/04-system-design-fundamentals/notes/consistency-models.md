# Consistency Models

In distributed systems, consistency models define the guarantees the system provides about the sequence of operations and the values that can be read.

## 1. Strong Consistency (Linearizability)
After a write operation is acknowledged, any subsequent read operation from any client must return the value of that write (or a more recent write). It makes a distributed system appear as though it were a single-node system.
- **Example:** Google Spanner, Etcd, ZooKeeper (for specific operations).

## 2. Eventual Consistency
The system guarantees that if no new updates are made to a specific data item, eventually all reads to that item will return the last updated value. Replicas might diverge for some time.
- **Example:** DNS, Amazon S3, Cassandra (by default).

## 3. Causal Consistency
If one operation "happens-before" another, they must be seen by all processes in that same order. If two operations are concurrent (no causal relationship), different processes can see them in different orders.
- **Example:** Comment threads on social media. If Alice replies to Bob's comment, everyone should see Bob's comment *before* Alice's.

## 4. Sequential Consistency
All operations from all processes are seen in some total order that is consistent with the order of operations from each individual process. It's weaker than strong consistency because it doesn't require "real-time" order, just "some" global order.

## 5. Client-centric Consistency Models
These focus on what an individual client sees, rather than the state across all nodes.
- **Read-Your-Writes:** A client can always read its own previous writes.
- **Monotonic Reads:** Once a client reads a certain value, they will never read an older value.
- **Bounded Staleness:** Reads are guaranteed to be no older than a certain time window or a certain number of versions.

---

## Comparison Table

| Consistency Model | Level of Guarantee | Latency | Complexity |
| :--- | :--- | :--- | :--- |
| **Strong** | Highest | Highest (sync replicas) | Highest |
| **Causal** | Medium | Medium | Medium (tracking deps) |
| **Eventual** | Lowest | Lowest (async replicas) | Lowest |

## Why not always use Strong Consistency?
Strong consistency usually requires synchronization across nodes (like Paxos, Raft, or 2PC), which significantly increases latency and reduces the availability of the system (see CAP theorem). Many high-scale systems (like social media feeds) prefer Eventual Consistency for performance.

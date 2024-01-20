# CAP Theorem

The CAP theorem states that in a distributed system, you can only provide two out of the following three guarantees:

## 1. Consistency (C)
Every read receives the most recent write or an error. In a consistent system, all nodes see the same data at the same time. This is "strong consistency".

## 2. Availability (A)
Every request receives a (non-error) response, without the guarantee that it contains the most recent write. The system remains operational even if some nodes are down.

## 3. Partition Tolerance (P)
The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes. In modern distributed systems, **P is non-negotiable** because network failures will happen.

---

## The Trade-off

Since Partition Tolerance (P) is required in any distributed system, the choice is usually between:

### CP (Consistency and Partition Tolerance)
If a partition occurs, the system will return an error or time out to ensure consistency. It sacrifices availability to maintain correctness.
- **Example:** Google Spanner, MongoDB (with majority read/write), HBase.

### AP (Availability and Partition Tolerance)
If a partition occurs, the system will continue to serve requests from any available node, even if the data might be stale. It sacrifices consistency to ensure the system is always up.
- **Example:** Cassandra, DynamoDB (with eventual consistency), CouchDB.

## Real Examples

### 1. ATM Withdrawals (AP vs CP)
- **CP:** If the ATM cannot reach the bank's central server, it refuses to give you money (sacrifices Availability for Consistency).
- **AP:** If the ATM cannot reach the bank's central server, it allows you to withdraw up to a certain limit (e.g., $200) anyway. It later reconciles the balance (sacrifices Consistency for Availability).

### 2. E-commerce Inventory
- **CP:** When you click "Buy", the system locks the item across all replicas to ensure it's not oversold. If one replica is unreachable, the purchase fails.
- **AP:** You can click "Buy", and the system says "Success". Later, you might get an email saying "Actually, we ran out of stock, here's a refund." (Eventual consistency).

## Common Misconceptions
- **"PACELC" is a better model:** CAP only describes what happens when there is a partition (P). PACELC extends this: "In case of **P**artition, choose between **A**vailability and **C**onsistency; **E**lse (no partition), choose between **L**atency and **C**onsistency."
- **Consistency in CAP is NOT ACID Consistency:** CAP Consistency is about the state of replicas (linearizability), while ACID Consistency is about database transactions and integrity constraints.

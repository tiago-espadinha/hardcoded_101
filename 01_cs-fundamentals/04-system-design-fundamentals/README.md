# System Design Studio

A collection of system design documents and toy implementations of distributed system primitives.

## Features
- **Design Documents**: Detailed architectural breakdowns of common systems (URL Shortener, Twitter Feed, etc.).
- **Distributed Primitives**: Working implementations of Bloom Filters, Consistent Hashing, LRU Cache, Message Queues, Rate Limiters, and Write-Ahead Logs (WAL).
- **Core Concepts**: Study notes on CAP theorem, consistency models, and database indexing.

## Learning Objectives
- Design scalable systems using core architectural principles (CAP theorem, PACELC).
- Implement distributed system primitives like Bloom Filters and Consistent Hashing.
- Understand the trade-offs between different consistency models and caching strategies.
- Learn to estimate capacity and identify single points of failure.

## Project Structure
- `designs/`: Markdown documents with requirements, capacity estimation, and trade-offs.
- `implementations/`: Python implementations of distributed system components.
- `notes/`: Concise study notes on core system design concepts.

## Requirements
- Python 3.10+

## How to Run
Each implementation in `implementations/` includes a `demo.py` script:
```bash
python implementations/rate_limiter/demo.py
```

## Testing
Run individual demos to verify primitive behavior:
```bash
python implementations/consistent_hashing/demo.py
```
# Design 03: File Storage (Dropbox-like)

## Requirements
- **Functional requirements**:
  - Users can upload and download files from any device.
  - Automatic synchronization across multiple devices.
  - File versioning and history (recovery of deleted/previous versions).
  - Support for large files via chunked uploads.
  - Offline editing and sync when back online.
- **Non-functional requirements**:
  - **High Durability**: Files must not be lost (99.999999999% target).
  - **High Availability**: 99.9% uptime for access.
  - **Scalability**: Handle 50M users, 10M DAU.
  - **Storage Efficiency**: Deduplication to minimize redundant data.
  - **Consistency**: Strong consistency for file metadata across devices.

## Capacity Estimation
- **Users**: 50M total, 10M Daily Active Users (DAU).
- **Storage**: Avg 10GB per user. Total capacity: 50M * 10GB = 500 PB.
- **File size**: Avg 1MB. Total files: 500PB / 1MB = 500 Billion files.
- **Writes/Uploads**: 10M DAU * 2 uploads/day = 20M uploads/day ≈ 230 uploads/sec.
- **Reads/Downloads**: 10M DAU * 5 downloads/day = 50M downloads/day ≈ 580 downloads/sec.
- **Bandwidth**: 230 uploads/sec * 1MB = 230 MB/s (Inbound). 580 * 1MB = 580 MB/s (Outbound).

## High-Level Architecture
```
[Client App] <-> [Load Balancer] <-> [API Gateway]
      |               |                  |
      |        [Block Service] <--> [Object Storage (S3)]
      |               |                  |
      |        [Metadata Service] <--> [Metadata DB (SQL)]
      |               |                  |
      |        [Sync Service] <-----> [Message Queue (Kafka)]
      |                                  |
      +------> [Notification Service] <--+
```
- **Block Service**: Handles file chunking, deduplication, and streaming to/from Object Storage.
- **Metadata Service**: Manages file names, paths, versions, and user permissions.
- **Object Storage**: S3-compatible store for raw file chunks (blocks).
- **Sync Service**: Compares local vs remote metadata to determine what needs to be transferred.
- **Notification Service**: Uses WebSockets or Long Polling to notify clients of remote changes.

## Data Model
- **Table: `files`** (Relational for ACID on metadata)
  - `file_id` (PK), `user_id` (FK), `file_name`, `path`, `is_directory`, `latest_version`.
- **Table: `file_versions`**
  - `version_id` (PK), `file_id` (FK), `checksum`, `size`, `created_at`.
- **Table: `blocks`**
  - `block_id` (PK/Hash), `version_id` (FK), `block_order`, `storage_path`.
- **Why this schema**: Relational DB ensures that file moves and renames are atomic. Versioning is tracked separately to allow easy rollbacks.

## Key Design Decisions
1. **Chunking Strategy**: Fixed-size (4MB) vs Variable-size (CDC - Content Defined Chunking). Chose **Variable-size chunking** to improve deduplication efficiency when users insert bytes in the middle of a file.
2. **Metadata Storage**: Chose **SQL (PostgreSQL/MySQL)** with sharding over NoSQL. ACID compliance is critical for file system operations (e.g., atomic moves/renames).
3. **Delta Sync**: Only upload the specific chunks that changed rather than the whole file. This reduces bandwidth and improves perceived latency.

## Bottlenecks & How to Scale
1. **Metadata DB Scaling**: As the number of files grows into billions, a single DB will fail. Use **Database Sharding** based on `user_id`.
2. **Global Latency**: Use **Edge Caching/CDNs** for frequently accessed blocks and deploy "Block Servers" in multiple geographical regions.
3. **Metadata Hotspots**: Use **Redis** to cache file metadata for active users to reduce DB read load.

## What I Would Do Differently at 10x Scale
- Transition to a **Global Multi-Master Metadata Store** (like Spanner) to handle cross-region synchronization more gracefully.
- Implement **Cold Storage Tiers** (like S3 Glacier) for files that haven't been accessed in over 6 months to reduce costs.
- Use **Machine Learning** to predict which files a user might open next based on their history and pre-fetch them to the local cache.

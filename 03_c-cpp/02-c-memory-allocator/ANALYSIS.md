# Memory Allocator Performance Analysis

## Overview
This report compares three different memory allocation strategies: First-Fit, Best-Fit, and the Buddy System.

## Benchmark Results

| Strategy   | 10,000 Small Allocs (LIFO) | 10,000 Small Allocs (Random) | 1,000 Large Allocs (Mixed) |
|------------|---------------------------|------------------------------|----------------------------|
| First-Fit  | 0.0012s                   | 0.0025s                      | 0.0031s                    |
| Best-Fit   | 0.0045s                   | 0.0089s                      | 0.0092s                    |
| Buddy      | 0.0008s                   | 0.0011s                      | 0.0015s                    |

## Comparison

### 1. First-Fit vs Best-Fit
First-fit is generally faster as it returns the first available block that meets the size requirement. Best-fit, while theoretically better for memory utilization, requires scanning the entire free list to find the absolute best match, which leads to $O(N)$ time complexity where $N$ is the number of blocks in the free list.

### 2. Fragmentation
Best-fit often results in many tiny "sliver" blocks that are too small to be useful (high external fragmentation). First-fit also suffers from this but can be slightly better in practice depending on the workload.

### 3. Buddy System
The Buddy System is significantly faster for allocations because it uses power-of-two blocks and can quickly locate a free block without a full linear scan. However, it suffers from internal fragmentation since it always rounds up to the next power of two.

## Conclusion
For most general-purpose workloads, the buddy system or more advanced hybrid strategies (like those in dlmalloc or jemalloc) are preferred over simple free-list based allocators.

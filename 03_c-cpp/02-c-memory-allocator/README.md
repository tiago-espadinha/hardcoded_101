# Module Name: C Memory Allocator

A custom memory allocator in C that replaces the system malloc/free with three different strategies: First-Fit, Best-Fit, and the Buddy System.

## Features
- **Multiple Strategies**: Implements First-Fit, Best-Fit, and Buddy System allocation.
- **Fixed Arena**: Uses a 32MB fixed-size arena for memory management.
- **Fragmentation Analysis**: Tools to measure and compare external fragmentation across strategies.
- **Benchmarking**: Performance comparison against system malloc under various workloads.

## Learning Objectives
- Implement heap allocator internals from scratch.
- Measure and reason about external fragmentation.
- Understand why different workloads favour different allocation strategies.

## Project Structure
- `allocator.h`: Shared interface for all allocators.
- `first_fit.c`: Implementation of the First-Fit strategy.
- `best_fit.c`: Implementation of the Best-Fit strategy.
- `buddy.c`: Implementation of the Buddy System strategy.
- `tests/`: Suite of correctness and fragmentation tests.
- `benchmark.c`: Performance measurement and comparison tool.
- `ANALYSIS.md`: Detailed analysis of the different allocation strategies.

## Requirements
- C17 compatible compiler (gcc/clang)
- Make

## How to Run
Compile and run the benchmark:
```bash
make benchmarks
```

## Testing
Run the correctness tests:
```bash
make tests
```

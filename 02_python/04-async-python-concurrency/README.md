# Module Name: Async Python Mastery

Learn and demonstrate Python's concurrency primitives through working, benchmarked examples.

## Features
- **Threading Mastery**: Efficient I/O-bound task handling with threads and thread pools.
- **Multiprocessing Power**: True parallelism for CPU-bound tasks using multiple processes and shared memory.
- **Asyncio Excellence**: Modern structured concurrency with asyncio, including HTTP, file I/O, and advanced patterns.
- **Capstone Projects**: Real-world applications like an async web crawler, task queue, and high-throughput API client.

## Learning Objectives
- Understand the GIL and why threads help I/O but not CPU-bound Python.
- Know when to use threads, processes, or async for any given problem.
- Write async code that handles backpressure, cancellation, and timeouts correctly.

## Project Structure
- `threading_examples/`: Core threading concepts and thread pools.
- `multiprocessing_examples/`: Parallel processing and shared memory.
- `asyncio_examples/`: Coroutines, async HTTP, and structured concurrency.
- `projects/`: Real-world capstone projects.
- `benchmarks/`: Performance comparisons across all concurrency models.

## Requirements
- Python 3.11+
- `aiohttp`, `aiofiles`, `numpy`, `rich`, `requests`

## How to Run
Run any individual example:
```bash
python asyncio_examples/01_coroutines.py
```

## Testing
Run benchmarks to see the difference:
```bash
python benchmarks/run_all.py
```

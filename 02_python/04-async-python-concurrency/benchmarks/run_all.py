#!/usr/bin/env python3
"""
benchmarks/run_all.py
Benchmark script comparing all approaches for:
- I/O-bound: downloading 100 URLs
- CPU-bound: hashing 1000 large strings
Output a Rich Table: approach | total_time | speedup | notes
"""

import asyncio
import time
import statistics
import requests
import hashlib
import concurrent.futures
from typing import List, Tuple
import aiohttp
import aiofiles
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

try:
    from rich.table import Table
    from rich.console import Console
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Warning: Rich not installed. Using simple table format.")

# Import our own modules for comparison
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

def create_test_strings(num_strings: int = 1000, string_size: int = 1000000) -> List[str]:
    """Create test strings for CPU-bound hashing benchmarks."""
    import random
    import string
    return [''.join(random.choices(string.ascii_letters + string.digits, k=string_size)) 
            for _ in range(num_strings)]

def hash_string_sha256(data: str) -> str:
    """Compute SHA-256 hash of a string."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# I/O-bound benchmarks (downloading URLs)
def run_io_sequential(urls: List[str]) -> float:
    """Download URLs sequentially using requests."""
    start = time.time()
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except Exception:
            pass  # Continue even if individual requests fail
    return time.time() - start

def run_io_threadpool(urls: List[str], max_workers: int = 10) -> float:
    """Download URLs using ThreadPoolExecutor."""
    def fetch_url(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return True
        except Exception:
            return False
    
    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        list(executor.map(fetch_url, urls))
    return time.time() - start

async def run_io_asyncio(urls: List[str], max_concurrent: int = 10) -> float:
    """Download URLs using asyncio and aiohttp."""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def fetch_url(session, url):
        async with semaphore:
            try:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    await response.read()
                    return True
            except Exception:
                return False
    
    start = time.time()
    connector = aiohttp.TCPConnector(limit=100, limit_per_host=20)
    timeout = aiohttp.ClientTimeout(total=10)
    
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)
    
    return time.time() - start

# CPU-bound benchmarks (hashing strings)
def run_cpu_sequential(strings: List[str]) -> float:
    """Hash strings sequentially."""
    start = time.time()
    for s in strings:
        hash_string_sha256(s)
    return time.time() - start

def _hash_chunk(string_chunk):
    """Hash a chunk of strings (top-level function for pickling)."""
    return [hash_string_sha256(s) for s in string_chunk]

def run_cpu_multiprocessing(strings: List[str], num_processes: int = 4) -> float:
    """Hash strings using multiprocessing.Process."""
    # Split work among processes
    chunk_size = len(strings) // num_processes
    chunks = [strings[i:i + chunk_size] for i in range(0, len(strings), chunk_size)]
    
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        list(executor.map(_hash_chunk, chunks))
    return time.time() - start

def run_cpu_processpool(strings: List[str], max_workers: int = 4) -> float:
    """Hash strings using ProcessPoolExecutor (same as above but explicit)."""
    return run_cpu_multiprocessing(strings, max_workers)

async def run_cpu_asyncio_with_executor(strings: List[str], max_workers: int = 4) -> float:
    """Hash strings using asyncio with run_in_executor (ThreadPoolExecutor)."""
    start = time.time()
    loop = asyncio.get_event_loop()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        tasks = [
            loop.run_in_executor(executor, hash_string_sha256, s)
            for s in strings
        ]
        await asyncio.gather(*tasks)
    
    return time.time() - start

def print_simple_table(headers: List[str], rows: List[List[str]]):
    """Print a simple table without Rich."""
    # Determine column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))
    
    # Print header
    header_row = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    separator = "-+-".join("-" * w for w in col_widths)
    print(header_row)
    print(separator)
    
    # Print rows
    for row in rows:
        print(" | ".join(cell.ljust(w) for cell, w in zip(row, col_widths)))

def main():
    print("=== Async Python Concurrency Benchmarks ===")
    print("Comparing different approaches for I/O-bound and CPU-bound tasks\n")
    
    # Create test data
    print("Creating test data...")
    
    # I/O-bound test data (URLs)
    # Using httpbin.org/delay/ with short delays for reasonable test time
    io_urls = [f"http://httpbin.org/delay/{i%3 + 1}" for i in range(10)]  # 10 URLs
    
    # CPU-bound test data (strings for hashing)
    # Further increased size to see parallelism benefits
    cpu_strings = create_test_strings(num_strings=1000, string_size=200000)  # 2000 strings of 200K chars
    
    print(f"I/O-bound: {len(io_urls)} URLs to httpbin.org/delay/")
    print(f"CPU-bound: {len(cpu_strings)} strings of {len(cpu_strings[0]) if cpu_strings else 0} characters\n")
    
    # Benchmark I/O-bound tasks
    print("--- I/O-Bound Benchmarks (Downloading URLs) ---")
    io_results = []
    
    # Sequential
    io_time = run_io_sequential(io_urls)
    io_results.append(("Sequential (requests)", io_time, 1.0, "Baseline"))
    
    # ThreadPoolExecutor
    io_time = run_io_threadpool(io_urls, max_workers=10)
    speedup = io_results[0][1] / io_time if io_time > 0 else 0
    io_results.append(("ThreadPoolExecutor(10)", io_time, speedup, "Good for I/O-bound"))
    
    # AsyncIO
    io_time = asyncio.run(run_io_asyncio(io_urls, max_concurrent=10))
    speedup = io_results[0][1] / io_time if io_time > 0 else 0
    io_results.append(("AsyncIO (aiohttp, 10)", io_time, speedup, "Best for I/O-bound"))
    
    # Benchmark CPU-bound tasks
    print("\n--- CPU-Bound Benchmarks (Hashing Strings) ---")
    cpu_results = []
    
    # Sequential
    cpu_time = run_cpu_sequential(cpu_strings)
    cpu_results.append(("Sequential", cpu_time, 1.0, "Baseline"))
    
    # Multiprocessing
    cpu_time = run_cpu_multiprocessing(cpu_strings, num_processes=4)
    speedup = cpu_results[0][1] / cpu_time if cpu_time > 0 else 0
    cpu_results.append(("Multiprocessing(4)", cpu_time, speedup, "Good for CPU-bound"))
    
    # ProcessPoolExecutor
    cpu_time = run_cpu_processpool(cpu_strings, max_workers=4)
    speedup = cpu_results[0][1] / cpu_time if cpu_time > 0 else 0
    cpu_results.append(("ProcessPoolExecutor(4)", cpu_time, speedup, "Same as above"))
    
    # AsyncIO with ThreadPoolExecutor (not ideal for CPU-bound)
    cpu_time = asyncio.run(run_cpu_asyncio_with_executor(cpu_strings, max_workers=4))
    speedup = cpu_results[0][1] / cpu_time if cpu_time > 0 else 0
    cpu_results.append(("AsyncIO + ThreadPool(4)", cpu_time, speedup, "Not ideal for CPU-bound"))
    
    # Print results
    if RICH_AVAILABLE:
        console = Console()
        
        # I/O-bound table
        io_table = Table(title="I/O-Bound Task: Downloading 30 URLs", box=box.ROUNDED)
        io_table.add_column("Approach", style="cyan")
        io_table.add_column("Total Time (s)", style="magenta")
        io_table.add_column("Speedup", style="green")
        io_table.add_column("Notes", style="yellow")
        
        for approach, total_time, speedup, notes in io_results:
            io_table.add_row(
                approach,
                f"{total_time:.2f}",
                f"{speedup:.2f}x",
                notes
            )
        
        console.print(io_table)
        
        # CPU-bound table
        cpu_table = Table(title="CPU-Bound Task: Hashing 100 Strings (10K chars each)", box=box.ROUNDED)
        cpu_table.add_column("Approach", style="cyan")
        cpu_table.add_column("Total Time (s)", style="magenta")
        cpu_table.add_column("Speedup", style="green")
        cpu_table.add_column("Notes", style="yellow")
        
        for approach, total_time, speedup, notes in cpu_results:
            cpu_table.add_row(
                approach,
                f"{total_time:.2f}",
                f"{speedup:.2f}x",
                notes
            )
        
        console.print(cpu_table)
    else:
        # Simple table format
        print("--- I/O-Bound Results ---")
        print_simple_table(
            ["Approach", "Total Time (s)", "Speedup", "Notes"],
            [[a, f"{t:.2f}", f"{s:.2f}x", n] for a, t, s, n in io_results]
        )
        
        print("\n--- CPU-Bound Results ---")
        print_simple_table(
            ["Approach", "Total Time (s)", "Speedup", "Notes"],
            [[a, f"{t:.2f}", f"{s:.2f}x", n] for a, t, s, n in cpu_results]
        )
    
    print("\n=== Key Takeaways ===")
    print("I/O-bound tasks: ThreadPoolExecutor and AsyncIO significantly outperform sequential")
    print("CPU-bound tasks: Multiprocessing/ProcessPoolExecutor needed to bypass GIL")
    print("AsyncIO with ThreadPoolExecutor helps but doesn't solve CPU-bound limitations")
    print("Choose the right tool for the problem: threads for I/O, processes for CPU, async for high-concurrency I/O")

if __name__ == "__main__":
    main()
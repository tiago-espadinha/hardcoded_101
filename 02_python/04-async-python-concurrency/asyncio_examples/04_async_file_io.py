import asyncio
import aiofiles
import time
import os
from concurrent.futures import ThreadPoolExecutor

def create_dummy_files(num_files):
    os.makedirs("dummy_files", exist_ok=True)
    for i in range(num_files):
        with open(f"dummy_files/file_{i}.txt", "w") as f:
            f.write(f"This is content for file {i} " * 1000)

def sync_read(filename):
    with open(filename, "r") as f:
        return f.read()

def run_sync(filenames):
    start = time.perf_counter()
    for filename in filenames:
        sync_read(filename)
    return time.perf_counter() - start

def run_threads(filenames):
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=20) as executor:
        list(executor.map(sync_read, filenames))
    return time.perf_counter() - start

async def async_read(filename):
    async with aiofiles.open(filename, mode='r') as f:
        return await f.read()

async def run_async(filenames):
    start = time.perf_counter()
    tasks = [async_read(filename) for filename in filenames]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start

if __name__ == "__main__":
    num_files = 100
    create_dummy_files(num_files)
    filenames = [f"dummy_files/file_{i}.txt" for i in range(num_files)]
    
    print(f"Reading {num_files} files...")
    
    t1 = run_sync(filenames)
    print(f"Sync Read:   {t1:.4f}s")
    
    t2 = run_threads(filenames)
    print(f"Thread Pool: {t2:.4f}s")
    
    t3 = asyncio.run(run_async(filenames))
    print(f"Async Read:  {t3:.4f}s")
    
    # Cleanup
    for f in filenames: os.remove(f)
    os.rmdir("dummy_files")

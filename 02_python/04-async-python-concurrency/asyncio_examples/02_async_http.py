import asyncio
import aiohttp
import requests
import time
import random

async def fetch_with_retry(session, url, semaphore, retries=3):
    async with semaphore:
        for attempt in range(retries):
            try:
                async with session.get(url, timeout=10) as response:
                    return await response.text()
            except Exception as e:
                if attempt == retries - 1:
                    return f"Error: {e}"
                # Exponential backoff with jitter
                wait_time = (2 ** attempt) + random.random()
                await asyncio.sleep(wait_time)

async def run_async_benchmark(urls):
    semaphore = asyncio.Semaphore(10) # Max 10 concurrent requests
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_retry(session, url, semaphore) for url in urls]
        return await asyncio.gather(*tasks)

def run_sync_benchmark(urls):
    results = []
    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            results.append(r.text)
        except Exception as e:
            results.append(str(e))
    return results

if __name__ == "__main__":
    urls = [f"https://httpbin.org/delay/{i % 2}" for i in range(20)]
    
    print(f"Benchmarking 20 URLs...")
    
    # Sync
    start = time.perf_counter()
    run_sync_benchmark(urls[:5]) # Only 5 for sync to save time
    sync_time = (time.perf_counter() - start) * 4 # Extrapolate to 20
    print(f"Sync (Extrapolated): {sync_time:.2f}s")
    
    # Async
    start = time.perf_counter()
    asyncio.run(run_async_benchmark(urls))
    async_time = time.perf_counter() - start
    print(f"Async (with Semaphore 10): {async_time:.2f}s")
    print(f"Speedup: {sync_time/async_time:.2f}x")

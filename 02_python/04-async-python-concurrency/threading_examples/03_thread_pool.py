import concurrent.futures
import requests
import time

def fetch_url(url):
    start_time = time.perf_counter()
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
    except Exception as e:
        status = str(e)
    end_time = time.perf_counter()
    return url, status, end_time - start_time

def run_benchmark(urls, max_workers=None):
    start_time = time.perf_counter()
    results = []
    
    if max_workers == 1:
        # Sequential
        for url in urls:
            results.append(fetch_url(url))
    else:
        # Thread Pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {executor.submit(fetch_url, url): url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url):
                results.append(future.result())
    
    end_time = time.perf_counter()
    return end_time - start_time, results

if __name__ == "__main__":
    # URLs with controllable latency
    urls = [f"https://httpbin.org/delay/{i % 2}" for i in range(20)]
    
    print(f"Benchmarking 20 URLs...")
    
    # Sequential (simulated by 1 worker for benchmark consistency)
    t1, _ = run_benchmark(urls, max_workers=1)
    print(f"Sequential: {t1:.2f}s")
    
    # 5 Threads
    t5, _ = run_benchmark(urls, max_workers=5)
    print(f"ThreadPool (5): {t5:.2f}s")
    
    # 20 Threads
    t20, _ = run_benchmark(urls, max_workers=20)
    print(f"ThreadPool (20): {t20:.2f}s")
    
    # Detailed results for the fastest run
    print("\nSample timings (from 20-thread run):")
    _, results = run_benchmark(urls[:5], max_workers=5)
    for url, status, duration in results:
        print(f"  {url} -> {status} in {duration:.2f}s")

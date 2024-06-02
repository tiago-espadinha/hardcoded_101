import hashlib
import multiprocessing
import concurrent.futures
import time
import os

def compute_hash(data):
    return hashlib.sha256(data).hexdigest()

def worker_task(num_hashes):
    # Each task computes a set number of hashes of random 1MB chunks
    for _ in range(num_hashes):
        data = os.urandom(1024 * 1024) # 1MB
        compute_hash(data)
    return num_hashes

def benchmark_processes(total_hashes, num_processes):
    hashes_per_proc = total_hashes // num_processes
    start_time = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(worker_task, hashes_per_proc) for _ in range(num_processes)]
        # Handle remainder
        if total_hashes % num_processes != 0:
            futures.append(executor.submit(worker_task, total_hashes % num_processes))
        
        for future in concurrent.futures.as_completed(futures):
            future.result()
            
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    total_hashes = 1000 # Reduced for demonstration purposes
    print(f"Hashing {total_hashes} strings of 1MB each...")
    
    # Single process
    t1 = benchmark_processes(total_hashes, 1)
    print(f"Single Process: {t1:.2f}s")
    
    # 2 Processes
    t2 = benchmark_processes(total_hashes, 2)
    print(f"2 Processes:    {t2:.2f}s (Speedup: {t1/t2:.2f}x)")
    
    # 4 Processes
    t4 = benchmark_processes(total_hashes, 4)
    print(f"4 Processes:    {t4:.2f}s (Speedup: {t1/t4:.2f}x)")
    
    # Auto (CPU count)
    num_cpus = multiprocessing.cpu_count()
    tc = benchmark_processes(total_hashes, num_cpus)
    print(f"Auto ({num_cpus} procs): {tc:.2f}s (Speedup: {t1/tc:.2f}x)")

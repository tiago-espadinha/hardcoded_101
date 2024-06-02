import threading
import time
import queue
import random

def race_condition_demo(n_threads, n_iterations):
    counter = 0
    def worker():
        nonlocal counter
        for _ in range(n_iterations):
            temp = counter
            # Force context switch
            time.sleep(0.000001)
            counter = temp + 1
    
    threads = [threading.Thread(target=worker) for _ in range(n_threads)]
    start_time = time.perf_counter()
    for t in threads: t.start()
    for t in threads: t.join()
    end_time = time.perf_counter()
    return counter, end_time - start_time

def lock_demo(n_threads, n_iterations):
    counter = 0
    lock = threading.Lock()
    def worker():
        nonlocal counter
        for _ in range(n_iterations):
            with lock:
                temp = counter
                time.sleep(0.000001)
                counter = temp + 1
    
    threads = [threading.Thread(target=worker) for _ in range(n_threads)]
    start_time = time.perf_counter()
    for t in threads: t.start()
    for t in threads: t.join()
    end_time = time.perf_counter()
    return counter, end_time - start_time

def rlock_demo(n_threads, n_iterations):
    counter = 0
    lock = threading.RLock()
    def worker():
        nonlocal counter
        for _ in range(n_iterations):
            with lock:
                # Re-entrant lock allows multiple acquisitions by the same thread
                with lock:
                    temp = counter
                    time.sleep(0.000001)
                    counter = temp + 1
    
    threads = [threading.Thread(target=worker) for _ in range(n_threads)]
    start_time = time.perf_counter()
    for t in threads: t.start()
    for t in threads: t.join()
    end_time = time.perf_counter()
    return counter, end_time - start_time

def queue_demo(n_threads, n_iterations):
    # Producer-Consumer model for thread safety
    q = queue.Queue()
    counter = 0
    def worker():
        for _ in range(n_iterations):
            q.put(1)
            time.sleep(0.000001)
    
    threads = [threading.Thread(target=worker) for _ in range(n_threads)]
    start_time = time.perf_counter()
    for t in threads: t.start()
    
    # Simple consumer thread to increment counter
    def consumer():
        nonlocal counter
        total_items = n_threads * n_iterations
        for _ in range(total_items):
            item = q.get()
            counter += item
            q.task_done()
    
    c_thread = threading.Thread(target=consumer)
    c_thread.start()
    
    for t in threads: t.join()
    q.join()
    c_thread.join()
    end_time = time.perf_counter()
    return counter, end_time - start_time

if __name__ == "__main__":
    n_threads = 5
    n_iterations = 100
    expected = n_threads * n_iterations
    
    print(f"Testing with {n_threads} threads and {n_iterations} iterations per thread.")
    print("-" * 60)
    
    c1, t1 = race_condition_demo(n_threads, n_iterations)
    print(f"Race Condition: Final={c1} (Expected {expected}), Time={t1:.4f}s")
    
    c2, t2 = lock_demo(n_threads, n_iterations)
    print(f"Lock:           Final={c2} (Expected {expected}), Time={t2:.4f}s")
    
    c3, t3 = rlock_demo(n_threads, n_iterations)
    print(f"RLock:          Final={c3} (Expected {expected}), Time={t3:.4f}s")
    
    c4, t4 = queue_demo(n_threads, n_iterations)
    print(f"Queue:          Final={c4} (Expected {expected}), Time={t4:.4f}s")

import threading
import time
import random

def worker(id):
    sleep_time = random.uniform(0.1, 0.5)
    print(f"Thread {id} starting, will sleep for {sleep_time:.2f}s")
    time.sleep(sleep_time)
    print(f"Thread {id} finished")

def demo_basic_threads():
    print("--- Basic Threads Execution Order ---")
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print("All threads finished\n")

# Shared counter demo
counter = 0
lock = threading.Lock()

def increment_without_lock(n):
    global counter
    for _ in range(n):
        temp = counter
        time.sleep(0.000001) # Force context switch
        counter = temp + 1

def increment_with_lock(n):
    global counter
    for _ in range(n):
        with lock:
            temp = counter
            time.sleep(0.000001)
            counter = temp + 1

def demo_shared_memory():
    global counter
    print("--- Shared Memory Demo ---")
    n = 100
    
    counter = 0
    print(f"Incrementing without lock ({n} iterations per thread, 5 threads)...")
    threads = [threading.Thread(target=increment_without_lock, args=(n,)) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Final counter (without lock): {counter} (Expected {n*5})")

    counter = 0
    print(f"Incrementing with lock ({n} iterations per thread, 5 threads)...")
    threads = [threading.Thread(target=increment_with_lock, args=(n,)) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Final counter (with lock): {counter} (Expected {n*5})\n")

if __name__ == "__main__":
    demo_basic_threads()
    demo_shared_memory()

import threading
import time
import random
from rate_limiter import TokenBucketLimiter, SlidingWindowLimiter

# --- Configuration ---
NUM_REQUESTS = 1000
NUM_CLIENTS = 10
CLIENT_KEYS = [f"client_{i}" for i in range(NUM_CLIENTS)] # Unique keys for sliding window
REQUEST_INTERVAL_SECONDS = 0.01 # Average delay between requests to simulate load

# Token Bucket Limiter Configuration
TB_CAPACITY = 10 # Max bursts of 10 requests
TB_REFILL_RATE = 5 # 5 tokens per second (allowing 5 req/sec average)

# Sliding Window Limiter Configuration
SW_LIMIT = 5 # Max 5 requests
SW_WINDOW_SECONDS = 1 # per 1 second window

# --- Simulation Logic ---
def simulate_requests(limiter, client_keys: list, total_requests: int, results: dict):
    """
    Simulates requests from multiple clients against a given rate limiter.
    """
    passed_requests = 0
    blocked_requests = 0

    for _ in range(total_requests // len(client_keys)):
        for client_key in client_keys:
            if limiter.allow(client_key):
                passed_requests += 1
            else:
                blocked_requests += 1
            time.sleep(random.uniform(0.001, REQUEST_INTERVAL_SECONDS * 2)) # Simulate variable request arrival

    results["passed"] = passed_requests
    results["blocked"] = blocked_requests
    results["total"] = passed_requests + blocked_requests


if __name__ == "__main__":
    print("--- Rate Limiter Demo ---")
    print(f"Total Requests per limiter: {NUM_REQUESTS}")
    print(f"Number of Clients: {NUM_CLIENTS}")
    print(f"Avg Request Interval: {REQUEST_INTERVAL_SECONDS} seconds")
    print("-" * 40)

    # --- Token Bucket Limiter Demo ---
    print(f"--- Token Bucket Limiter (Capacity: {TB_CAPACITY}, Refill Rate: {TB_REFILL_RATE} req/s) ---")
    tb_limiter = TokenBucketLimiter(capacity=TB_CAPACITY, refill_rate=TB_REFILL_RATE)
    tb_results = {"passed": 0, "blocked": 0, "total": 0}
    tb_threads = []

    tb_start_time = time.monotonic()
    for _ in range(NUM_CLIENTS):
        # Token bucket is global, so all clients draw from the same bucket
        thread = threading.Thread(target=simulate_requests, args=(tb_limiter, ['global_key'], NUM_REQUESTS // NUM_CLIENTS, tb_results))
        tb_threads.append(thread)
        thread.start()

    for thread in tb_threads:
        thread.join()
    tb_end_time = time.monotonic()

    print(f"Simulation finished in {tb_end_time - tb_start_time:.2f} seconds.")
    print(f"Total Requests: {tb_results['total']}")
    print(f"Requests Passed: {tb_results['passed']}")
    print(f"Requests Blocked: {tb_results['blocked']}")
    print(f"Pass Rate: {(tb_results['passed'] / tb_results['total'] * 100):.2f}%")
    print("-" * 40)

    # --- Sliding Window Limiter Demo ---
    print(f"--- Sliding Window Limiter (Limit: {SW_LIMIT}, Window: {SW_WINDOW_SECONDS}s) ---")
    sw_limiter = SlidingWindowLimiter(limit=SW_LIMIT, window_seconds=SW_WINDOW_SECONDS)
    sw_results = {"passed": 0, "blocked": 0, "total": 0}
    sw_threads = []

    sw_start_time = time.monotonic()
    # Each client has its own rate limit in Sliding Window
    for i in range(NUM_CLIENTS):
        thread = threading.Thread(target=simulate_requests, args=(sw_limiter, [CLIENT_KEYS[i]], NUM_REQUESTS // NUM_CLIENTS, sw_results))
        sw_threads.append(thread)
        thread.start()

    for thread in sw_threads:
        thread.join()
    sw_end_time = time.monotonic()

    print(f"Simulation finished in {sw_end_time - sw_start_time:.2f} seconds.")
    print(f"Total Requests: {sw_results['total']}")
    print(f"Requests Passed: {sw_results['passed']}")
    print(f"Requests Blocked: {sw_results['blocked']}")
    print(f"Pass Rate: {(sw_results['passed'] / sw_results['total'] * 100):.2f}%")
    print("-" * 40)

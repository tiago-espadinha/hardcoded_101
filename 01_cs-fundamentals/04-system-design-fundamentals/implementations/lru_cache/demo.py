import time
import random
import threading
from lru_cache import LRUCache

# --- Configuration ---
CACHE_CAPACITY = 5
CACHE_TTL_SECONDS = 3 # Items expire after 3 seconds
NUM_REQUESTS = 1000
NUM_CLIENTS = 10
KEY_RANGE = 20 # Keys will be integers from 0 to KEY_RANGE-1
WRITE_PROBABILITY = 0.3 # Probability of a request being a 'put' operation

# --- Simulation Logic ---
def simulate_client_requests(cache: LRUCache, client_id: int, results: list):
    """
    Simulates cache requests (get/put) from a single client.
    Records hit/miss and total requests for this client.
    """
    local_hits = 0
    local_misses = 0
    local_puts = 0
    local_total_gets = 0

    for _ in range(NUM_REQUESTS // NUM_CLIENTS):
        key = str(random.randint(0, KEY_RANGE - 1)) # Simulate various keys

        if random.random() < WRITE_PROBABILITY:
            # Simulate a 'put' operation
            value = f"value_{key}_{time.time()}"
            cache.put(key, value)
            local_puts += 1
            # print(f"Client {client_id}: PUT key={key}, value={value}")
        else:
            # Simulate a 'get' operation
            local_total_gets += 1
            value = cache.get(key)
            if value is not None:
                local_hits += 1
                # print(f"Client {client_id}: GET hit for key={key}, value={value}")
            else:
                local_misses += 1
                # print(f"Client {client_id}: GET miss for key={key}")

        # Introduce a small delay to simulate real-world latency and allow TTL to work
        time.sleep(random.uniform(0.01, 0.05))

    results.append({
        "client_id": client_id,
        "hits": local_hits,
        "misses": local_misses,
        "puts": local_puts,
        "total_gets": local_total_gets
    })

if __name__ == "__main__":
    print(f"--- LRU Cache Simulation with TTL ---")
    print(f"Capacity: {CACHE_CAPACITY}, TTL: {CACHE_TTL_SECONDS} seconds")
    print(f"Total Requests: {NUM_REQUESTS}, Clients: {NUM_CLIENTS}, Key Range: {KEY_RANGE}")
    print(f"Write Probability: {WRITE_PROBABILITY*100}% (rest are GETs)")
    print("-" * 40)

    lru_cache = LRUCache(capacity=CACHE_CAPACITY, ttl_seconds=CACHE_TTL_SECONDS)
    threads = []
    client_results = []

    start_time = time.time()

    for i in range(NUM_CLIENTS):
        thread = threading.Thread(target=simulate_client_requests, args=(lru_cache, i + 1, client_results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    total_hits = sum(res["hits"] for res in client_results)
    total_misses = sum(res["misses"] for res in client_results)
    total_puts = sum(res["puts"] for res in client_results)
    total_gets = sum(res["total_gets"] for res in client_results)

    hit_rate = (total_hits / total_gets * 100) if total_gets > 0 else 0

    print("-" * 40)
    print(f"Simulation finished in {end_time - start_time:.2f} seconds.")
    print(f"Total GET Requests: {total_gets}")
    print(f"Total PUT Requests: {total_puts}")
    print(f"Total Hits: {total_hits}")
    print(f"Total Misses: {total_misses}")
    print(f"Hit Rate: {hit_rate:.2f}%")
    print(f"Final Cache Size: {lru_cache.size()}")
    print(f"Cache state: {lru_cache}")
    print("-" * 40)

    # Demonstrate TTL explicitly
    print("--- Demonstrating TTL ---")
    demo_cache = LRUCache(capacity=2, ttl_seconds=1)
    demo_cache.put("A", 1)
    demo_cache.put("B", 2)
    print(f"Cache after put A, B: {demo_cache}")
    time.sleep(0.5)
    print(f"Get A (should be fresh): {demo_cache.get('A')}")
    print(f"Cache after get A: {demo_cache}") # A moved to end
    time.sleep(0.7) # B should be expired, A should be close to expired
    print(f"Get B (should be expired, return None): {demo_cache.get('B')}")
    print(f"Cache after get B: {demo_cache}") # B removed
    time.sleep(0.5) # A should now be expired
    print(f"Get A (should be expired, return None): {demo_cache.get('A')}")
    print(f"Cache after get A: {demo_cache}") # A removed
    print("-------------------------")

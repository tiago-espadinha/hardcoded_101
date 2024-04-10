from multiprocessing import Process, Queue, Event
import time
import random

def producer(output_queue, num_items):
    """Stage 1: Generate data."""
    print("Stage 1: Producer starting...")
    for i in range(num_items):
        item = random.random()
        output_queue.put(item)
    # Signal completion
    output_queue.put(None)
    print("Stage 1: Producer finished.")

def transformer(input_queue, output_queue):
    """Stage 2: Transform data (e.g., square it)."""
    print("Stage 2: Transformer starting...")
    while True:
        item = input_queue.get()
        if item is None:
            output_queue.put(None)
            break
        transformed = item ** 2
        output_queue.put(transformed)
    print("Stage 2: Transformer finished.")

def aggregator(input_queue, result_event):
    """Stage 3: Aggregate results."""
    print("Stage 3: Aggregator starting...")
    total = 0
    count = 0
    while True:
        item = input_queue.get()
        if item is None:
            break
        total += item
        count += 1
    print(f"Stage 3: Aggregator finished. Count={count}, Total={total:.4f}")
    result_event.set()

def run_pipeline(num_items):
    q1 = Queue(maxsize=100)
    q2 = Queue(maxsize=100)
    done_event = Event()
    
    start_time = time.perf_counter()
    
    p1 = Process(target=producer, args=(q1, num_items))
    p2 = Process(target=transformer, args=(q1, q2))
    p3 = Process(target=aggregator, args=(q2, done_event))
    
    for p in [p1, p2, p3]: p.start()
    
    for p in [p1, p2]: p.join()
    done_event.wait()
    p3.join()
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"\nPipeline throughput: {num_items / duration:.2f} items/sec")

if __name__ == "__main__":
    num_items = 10000
    run_pipeline(num_items)

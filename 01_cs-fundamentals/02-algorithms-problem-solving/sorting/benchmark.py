import random
import time
from typing import List, Callable
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from counting_sort import counting_sort

def run_benchmark(name: str, func: Callable[[List[int]], List[int]], data: List[int]) -> float:
    """Runs a single sort function and returns the time taken."""
    # Work on a copy to avoid modifying the original data for other benchmarks
    data_copy = data.copy()
    start = time.perf_counter()
    func(data_copy)
    end = time.perf_counter()
    return end - start

def main():
    # Dataset: 10,000 random integers
    SIZE = 10000
    DATASET = [random.randint(0, 10000) for _ in range(SIZE)]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort),
        ("Python sorted()", sorted)
    ]
    
    print(f"Benchmarking {len(algorithms)} algorithms with {SIZE} elements...")
    print("-" * 45)
    print(f"{'Algorithm':<20} | {'Time (s)':<15}")
    print("-" * 45)
    
    results = []
    for name, func in algorithms:
        # Note: Bubble and Insertion Sort are O(n^2) and might be slow for 10k
        # But 10k should be manageable (a few seconds)
        duration = run_benchmark(name, func, DATASET)
        results.append((name, duration))
        print(f"{name:<20} | {duration:<15.6f}")
    
    print("-" * 45)

if __name__ == "__main__":
    main()

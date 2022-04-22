import random
import time
from typing import List
from utils.timer import timer

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list using the bubble sort algorithm.
    Time complexity: O(n^2) average and worst-case.
    Space complexity: O(1) auxiliary.
    
    Args:
        arr: The list of integers to sort.
        
    Returns:
        The sorted list (modified in-place).
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def visualise(arr: List[int]) -> None:
    """Prints each pass of bubble sort to stdout."""
    print(f"Original: {arr}")
    n = len(arr)
    temp = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                swapped = True
        print(f"Pass {i+1}:  {temp}")
        if not swapped:
            break

def benchmark() -> None:
    """Benchmarks bubble_sort against Python's sorted()."""
    test_data = [random.randint(0, 10000) for _ in range(1000)] # 10k is slow for bubble sort
    print("Benchmarking Bubble Sort (1,000 elements)...")
    
    data_copy = test_data.copy()
    start = time.perf_counter()
    bubble_sort(data_copy)
    end = time.perf_counter()
    print(f"Bubble Sort: {end - start:.6f} seconds")
    
    data_copy = test_data.copy()
    start = time.perf_counter()
    sorted(data_copy)
    end = time.perf_counter()
    print(f"Python sorted(): {end - start:.6f} seconds")

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    visualise(sample)
    # benchmark() # Uncomment to run benchmark

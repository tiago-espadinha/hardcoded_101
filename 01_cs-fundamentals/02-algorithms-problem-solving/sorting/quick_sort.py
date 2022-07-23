import random
import time
from typing import List
from utils.timer import timer

def quick_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list using the quick sort algorithm.
    Time complexity: O(n log n) average, O(n^2) worst-case.
    Space complexity: O(log n) auxiliary.
    
    Args:
        arr: The list of integers to sort.
        
    Returns:
        The sorted list (modified in-place).
    """
    _quick_sort(arr, 0, len(arr) - 1)
    return arr

def _quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pi = partition(arr, low, high)
        _quick_sort(arr, low, pi - 1)
        _quick_sort(arr, pi + 1, high)

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def visualise(arr: List[int]) -> None:
    """Prints each partition step of quick sort."""
    print(f"Original: {arr}")
    temp = arr.copy()
    
    def _vis_quick_sort(a, l, h):
        if l < h:
            pivot = a[h]
            print(f"Partitioning around pivot {pivot} in {a[l:h+1]}")
            pi = partition(a, l, h)
            print(f"Result: {a}")
            _vis_quick_sort(a, l, pi - 1)
            _vis_quick_sort(a, pi + 1, h)
            
    _vis_quick_sort(temp, 0, len(temp) - 1)

def benchmark() -> None:
    """Benchmarks quick_sort against Python's sorted()."""
    test_data = [random.randint(0, 10000) for _ in range(10000)]
    print("Benchmarking Quick Sort (10,000 elements)...")
    
    data_copy = test_data.copy()
    start = time.perf_counter()
    quick_sort(data_copy)
    end = time.perf_counter()
    print(f"Quick Sort: {end - start:.6f} seconds")
    
    data_copy = test_data.copy()
    start = time.perf_counter()
    sorted(data_copy)
    end = time.perf_counter()
    print(f"Python sorted(): {end - start:.6f} seconds")

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    visualise(sample)

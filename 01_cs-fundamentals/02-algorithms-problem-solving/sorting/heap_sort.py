import random
import time
from typing import List
from utils.timer import timer

def heap_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list using the heap sort algorithm.
    Time complexity: O(n log n) average and worst-case.
    Space complexity: O(1) auxiliary.
    
    Args:
        arr: The list of integers to sort.
        
    Returns:
        The sorted list (modified in-place).
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def heapify(arr: List[int], n: int, i: int) -> None:
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def visualise(arr: List[int]) -> None:
    """Prints each step of heap sort."""
    print(f"Original: {arr}")
    temp = arr.copy()
    n = len(temp)
    print("Building Max Heap...")
    for i in range(n // 2 - 1, -1, -1):
        heapify(temp, n, i)
        print(f"Heap: {temp}")
    print("Extracting elements...")
    for i in range(n - 1, 0, -1):
        temp[i], temp[0] = temp[0], temp[i]
        heapify(temp, i, 0)
        print(f"Extraction {n-i}: {temp}")

def benchmark() -> None:
    """Benchmarks heap_sort against Python's sorted()."""
    test_data = [random.randint(0, 10000) for _ in range(10000)]
    print("Benchmarking Heap Sort (10,000 elements)...")
    
    data_copy = test_data.copy()
    start = time.perf_counter()
    heap_sort(data_copy)
    end = time.perf_counter()
    print(f"Heap Sort: {end - start:.6f} seconds")
    
    data_copy = test_data.copy()
    start = time.perf_counter()
    sorted(data_copy)
    end = time.perf_counter()
    print(f"Python sorted(): {end - start:.6f} seconds")

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    visualise(sample)

import random
import time
from typing import List
from utils.timer import timer

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list using the insertion sort algorithm.
    Time complexity: O(n^2) average and worst-case, O(n) best-case.
    Space complexity: O(1) auxiliary.
    
    Args:
        arr: The list of integers to sort.
        
    Returns:
        The sorted list (modified in-place).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def visualise(arr: List[int]) -> None:
    """Prints each pass of insertion sort to stdout."""
    print(f"Original: {arr}")
    temp = arr.copy()
    for i in range(1, len(temp)):
        key = temp[i]
        j = i - 1
        while j >= 0 and key < temp[j]:
            temp[j + 1] = temp[j]
            j -= 1
        temp[j + 1] = key
        print(f"Pass {i}:  {temp}")

def benchmark() -> None:
    """Benchmarks insertion_sort against Python's sorted()."""
    test_data = [random.randint(0, 10000) for _ in range(10000)]
    print("Benchmarking Insertion Sort (10,000 elements)...")
    
    data_copy = test_data.copy()
    start = time.perf_counter()
    insertion_sort(data_copy)
    end = time.perf_counter()
    print(f"Insertion Sort: {end - start:.6f} seconds")
    
    data_copy = test_data.copy()
    start = time.perf_counter()
    sorted(data_copy)
    end = time.perf_counter()
    print(f"Python sorted(): {end - start:.6f} seconds")

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    visualise(sample)

import random
import time
from typing import List
from utils.timer import timer

def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list using the merge sort algorithm.
    Time complexity: O(n log n) average and worst-case.
    Space complexity: O(n) auxiliary.
    
    Args:
        arr: The list of integers to sort.
        
    Returns:
        The sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def visualise(arr: List[int]) -> None:
    """Prints progress of merge sort (recursive steps)."""
    print(f"Dividing: {arr}")
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = visualise(arr[:mid])
    right = visualise(arr[mid:])
    merged = merge(left, right)
    print(f"Merging:  {left} + {right} -> {merged}")
    return merged

def benchmark() -> None:
    """Benchmarks merge_sort against Python's sorted()."""
    test_data = [random.randint(0, 10000) for _ in range(10000)]
    print("Benchmarking Merge Sort (10,000 elements)...")
    
    start = time.perf_counter()
    merge_sort(test_data)
    end = time.perf_counter()
    print(f"Merge Sort: {end - start:.6f} seconds")
    
    start = time.perf_counter()
    sorted(test_data)
    end = time.perf_counter()
    print(f"Python sorted(): {end - start:.6f} seconds")

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    visualise(sample)
    # benchmark()

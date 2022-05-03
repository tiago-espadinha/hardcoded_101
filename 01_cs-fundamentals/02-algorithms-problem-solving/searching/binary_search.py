from typing import List, Optional

def binary_search_iterative(arr: List[int], target: int) -> Optional[int]:
    """
    Finds the index of a target value in a sorted array using an iterative approach.
    Time complexity: O(log n)
    Space complexity: O(1)
    
    Args:
        arr: The sorted list of integers to search.
        target: The value to find.
        
    Returns:
        The index of the target value if found, otherwise None.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return None

def binary_search_recursive(arr: List[int], target: int, low: int = 0, high: Optional[int] = None) -> Optional[int]:
    """
    Finds the index of a target value in a sorted array using a recursive approach.
    Time complexity: O(log n)
    Space complexity: O(log n) due to recursion stack.
    
    Args:
        arr: The sorted list of integers to search.
        target: The value to find.
        low: The lower bound of the search range.
        high: The upper bound of the search range.
        
    Returns:
        The index of the target value if found, otherwise None.
    """
    if high is None:
        high = len(arr) - 1
        
    if low > high:
        return None
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

if __name__ == "__main__":
    sample = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    
    print(f"Dataset: {sample}")
    print(f"Target:  {target}")
    
    iter_idx = binary_search_iterative(sample, target)
    rec_idx = binary_search_recursive(sample, target)
    
    print(f"Iterative index: {iter_idx}")
    print(f"Recursive index: {rec_idx}")
    
    missing_target = 6
    print(f"\nSearching for {missing_target} (not in list)...")
    print(f"Iterative index: {binary_search_iterative(sample, missing_target)}")
    print(f"Recursive index: {binary_search_recursive(sample, missing_target)}")

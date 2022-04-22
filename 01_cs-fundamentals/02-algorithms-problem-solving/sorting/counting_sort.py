from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of non-negative integers using the counting sort algorithm.
    Time complexity: O(n + k) where n is the number of elements and k is the range of input.
    Space complexity: O(n + k) auxiliary.
    
    Args:
        arr: The list of non-negative integers to sort.
        
    Returns:
        The sorted list.
    """
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    
    # Adjust for negative numbers if any, but counting sort is typically for non-negative
    # We'll handle a range starting from min_val to max_val
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store count of each element
    for x in arr:
        count[x - min_val] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output character array
    # To make it stable, we operate in reverse order
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output

if __name__ == "__main__":
    sample = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original: {sample}")
    sorted_sample = counting_sort(sample)
    print(f"Sorted:   {sorted_sample}")

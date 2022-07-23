"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
from typing import List

def max_subarray_brute_force(nums: List[int]) -> int:
    """
    Brute force solution.
    Check every possible subarray.
    Time complexity: O(n^2) - We have two nested loops to check all subarrays.
    Space complexity: O(1) - No extra space is used besides variables.
    """
    max_sum = float('-inf')
    n = len(nums)
    if n == 0:
        return 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

def max_subarray_optimized(nums: List[int]) -> int:
    """
    Optimized solution using Kadane's Algorithm.
    Iterate through the array, keeping track of the maximum sum ending at the current position.
    Time complexity: O(n) - A single pass through the array.
    Space complexity: O(1) - Only constant extra space is used.
    """
    max_so_far = float('-inf')
    max_ending_here = 0
    for num in nums:
        max_ending_here = max_ending_here + num
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

# Test cases
# Brute Force
assert max_subarray_brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray_brute_force([1]) == 1
assert max_subarray_brute_force([5, 4, -1, 7, 8]) == 23

# Optimized (Kadane's Algorithm)
assert max_subarray_optimized([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray_optimized([1]) == 1
assert max_subarray_optimized([5, 4, -1, 7, 8]) == 23
assert max_subarray_optimized([-1]) == -1
assert max_subarray_optimized([-2, -1]) == -1

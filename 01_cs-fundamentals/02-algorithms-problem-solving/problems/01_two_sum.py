"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum_brute_force(nums, target):
    """
    Brute force solution.
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_optimized(nums, target):
    """
    Optimized solution using a hash map.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Test cases
assert two_sum_brute_force([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_brute_force([3, 2, 4], 6) == [1, 2]
assert two_sum_brute_force([3, 3], 6) == [0, 1]

assert two_sum_optimized([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_optimized([3, 2, 4], 6) == [1, 2]
assert two_sum_optimized([3, 3], 6) == [0, 1]

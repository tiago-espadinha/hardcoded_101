"""
Given an array of integers `nums` containing `n + 1` integers where each integer
is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number.

You must solve the problem without modifying the array `nums` and using only
constant extra space.
"""
from typing import List

# Brute-force solution
def find_duplicate_brute(nums: List[int]) -> int:
    """
    Brute-force solution using a hash set.
    Time complexity: O(N), where N is the number of elements in nums.
    Space complexity: O(N) for the hash set.
    Note: This violates the "constant extra space" constraint.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1 # Should not be reached given the problem constraints

# Optimized solution (Floyd's Tortoise and Hare)
def find_duplicate_optimized(nums: List[int]) -> int:
    """
    Optimized solution using Floyd's cycle-finding algorithm.
    This problem can be mapped to finding a cycle in a linked list.
    The values in the array act as pointers.
    Time complexity: O(N).
    Space complexity: O(1).
    """
    # Phase 1: Find the intersection point of the two pointers.
    tortoise = nums[0]
    hare = nums[0]
    
    # The first `do-while` loop is guaranteed to have a cycle because of the
    # problem constraints (n+1 numbers in the range [1, n]).
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: Find the "entrance" to the cycle.
    # Reset one pointer to the start. The other stays at the intersection.
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

# Test cases
nums1 = [1,3,4,2,2]
# Cycle: 3 -> 2 -> 4 -> 2...
# Tortoise: 1 -> 3 -> 2 -> 4
# Hare:     1 -> 2 -> 2 -> 2
# Intersection at 2 is not correct logic.
# Let's trace it properly:
# 1. tortoise = nums[0] = 1, hare = nums[0] = 1
# Loop 1:
# tortoise = nums[1] = 3
# hare = nums[nums[1]] = nums[3] = 2
# Loop 2:
# tortoise = nums[3] = 2
# hare = nums[nums[2]] = nums[4] = 2
# tortoise == hare (both are 2). Intersection found.
#
# 2. ptr1 = nums[0] = 1, ptr2 = 2
# Loop 1:
# ptr1 = nums[1] = 3
# ptr2 = nums[2] = 4
# Loop 2:
# ptr1 = nums[3] = 2
# ptr2 = nums[4] = 2
# ptr1 == ptr2 (both are 2). Duplicate is 2.
assert find_duplicate_brute(nums1) == 2
assert find_duplicate_optimized(nums1) == 2

nums2 = [3,1,3,4,2]
# Cycle: 3 -> 4 -> 2 -> 3...
# 1. tortoise = 3, hare = 3
# Loop 1: t=nums[3]=4, h=nums[nums[3]]=nums[4]=2
# Loop 2: t=nums[4]=2, h=nums[nums[2]]=nums[3]=4
# Loop 3: t=nums[2]=3, h=nums[nums[4]]=nums[2]=3
# Intersection at 3.
#
# 2. ptr1 = 3, ptr2 = 3
# They are already equal, so the duplicate is 3.
assert find_duplicate_brute(nums2) == 3
assert find_duplicate_optimized(nums2) == 3

nums3 = [1,1]
assert find_duplicate_brute(nums3) == 1
assert find_duplicate_optimized(nums3) == 1

nums4 = [2,2,2,2,2]
assert find_duplicate_brute(nums4) == 2
assert find_duplicate_optimized(nums4) == 2

print("All test cases passed!")

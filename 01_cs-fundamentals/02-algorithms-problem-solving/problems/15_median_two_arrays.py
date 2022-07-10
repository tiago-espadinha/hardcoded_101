"""
15. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).
"""

# Brute Force Solution
def findMedianSortedArrays_brute_force(nums1, nums2):
    merged = sorted(nums1 + nums2)
    total = len(merged)
    if total % 2 == 1:
        return float(merged[total // 2])
    else:
        mid1 = merged[total // 2 - 1]
        mid2 = merged[total // 2]
        return (mid1 + mid2) / 2.0

# Complexity Analysis (Brute Force)
# Time Complexity: O((m+n) log(m+n)) due to sorting the merged array.
# Merging is O(m+n), sorting is O((m+n)log(m+n)).
# Space Complexity: O(m+n) to store the merged array.

# Optimized Solution (Binary Search)
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # Ensure nums1 is the smaller array to optimize binary search range
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m
    total_len = m + n
    half_len = (total_len + 1) // 2

    while low <= high:
        partition1 = (low + high) // 2
        partition2 = half_len - partition1

        # Get maxLeft1, minRight1, maxLeft2, minRight2
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]

        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Correct partition found, calculate median
            if total_len % 2 == 0:
                # Even number of elements
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            else:
                # Odd number of elements
                return float(max(maxLeft1, maxLeft2))
        elif maxLeft1 > minRight2:
            # Move left in nums1
            high = partition1 - 1
        else:
            # Move right in nums1
            low = partition1 + 1
    # Should not happen if inputs are sorted arrays
    raise ValueError("Input arrays are not sorted or invalid")


# Complexity Analysis (Optimized)
# Time Complexity: O(log(min(m, n))) because we perform binary search on the smaller array.
# Space Complexity: O(1) as we only use a few variables to store state.

# Test Cases
nums1 = [1, 3]
nums2 = [2]
assert findMedianSortedArrays(nums1, nums2) == 2.0, "Test Case 1 Failed"

nums1_2 = [1, 2]
nums2_2 = [3, 4]
assert findMedianSortedArrays(nums1_2, nums2_2) == 2.5, "Test Case 2 Failed"

nums1_3 = [0, 0]
nums2_3 = [0, 0]
assert findMedianSortedArrays(nums1_3, nums2_3) == 0.0, "Test Case 3 Failed"

nums1_4 = []
nums2_4 = [1]
assert findMedianSortedArrays(nums1_4, nums2_4) == 1.0, "Test Case 4 Failed"

nums1_5 = [2]
nums2_5 = []
assert findMedianSortedArrays(nums1_5, nums2_5) == 2.0, "Test Case 5 Failed"

print("All test cases pass")

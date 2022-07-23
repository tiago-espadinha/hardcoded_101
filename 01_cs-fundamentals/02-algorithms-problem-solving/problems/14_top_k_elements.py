"""
14. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.
"""
import collections
import heapq

# Brute Force
def topKFrequent_brute_force(nums, k):
    # 1. Count frequencies
    counts = collections.Counter(nums)
    # 2. Sort by frequency
    # .items() gives (element, count). We sort by count descending.
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    # 3. Take the top k elements
    return [item[0] for item in sorted_counts[:k]]

# Complexity Analysis (Brute Force)
# Time Complexity: O(U log U) where U is the number of unique elements in the array.
# The dominant step is sorting the frequencies.
# Space Complexity: O(U) to store the frequencies.

# Optimized Solution (Heap)
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == len(nums):
        return nums

    # 1. Build hash map: element -> its frequency
    counts = collections.Counter(nums)

    # 2. Build heap of size k
    # We use a min-heap. We push (frequency, element)
    heap = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap) # pop the smallest frequency

    # 3. Build output array
    return [num for freq, num in heap]

# Complexity Analysis (Optimized)
# Time Complexity: O(N log k), where N is the number of items in the array.
# collections.Counter takes O(N).
# The loop runs U times (number of unique elements). Heap push/pop is O(log k).
# So, O(N + U log k). If U is proportional to N, it's O(N log k).
# Space Complexity: O(U + k). O(U) for the hash map and O(k) for the heap.

# Test Cases
# Note: The order of output may vary for elements with the same frequency.
# We sort the result to make tests deterministic.
nums1, k1 = [1,1,1,2,2,3], 2
result1 = topKFrequent(nums1, k1)
result1.sort()
assert result1 == [1, 2], "Test Case 1 Failed"

nums2, k2 = [1], 1
result2 = topKFrequent(nums2, k2)
assert result2 == [1], "Test Case 2 Failed"

nums3, k3 = [3,0,1,0], 1
result3 = topKFrequent(nums3, k3)
assert result3 == [0], "Test Case 3 Failed"

nums4, k4 = [4,1,-1,2,-1,2,3], 2
result4 = topKFrequent(nums4, k4)
result4.sort()
assert result4 == [-1, 2], "Test Case 4 Failed"

print("All test cases pass")

"""
Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals, and return an array of the non-overlapping intervals that
cover all the intervals in the input.
"""
from typing import List

# Brute-force solution
def merge_intervals_brute(intervals: List[List[int]]) -> List[List[int]]:
    """
    Brute-force approach by comparing every interval with every other interval.
    Time complexity: O(N^2), where N is the number of intervals.
    Space complexity: O(N) for storing the merged intervals.
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        if not merged:
            merged.append(interval)
        else:
            was_merged = False
            for i in range(len(merged)):
                # Check for overlap
                if max(merged[i][0], interval[0]) <= min(merged[i][1], interval[1]):
                    merged[i][0] = min(merged[i][0], interval[0])
                    merged[i][1] = max(merged[i][1], interval[1])
                    was_merged = True
                    break
            if not was_merged:
                merged.append(interval)
    
    # Second pass to merge any intervals that might now overlap
    # This is inefficient and the main reason for O(N^2)
    can_merge = True
    while can_merge:
        can_merge = False
        i = 0
        while i < len(merged):
            j = i + 1
            while j < len(merged):
                interval1 = merged[i]
                interval2 = merged[j]
                if max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1]):
                    merged[i][0] = min(interval1[0], interval2[0])
                    merged[i][1] = max(interval1[1], interval2[1])
                    merged.pop(j)
                    can_merge = True
                else:
                    j += 1
            i += 1
            
    return sorted(merged, key=lambda x: x[0])


# Optimized solution
def merge_intervals_optimized(intervals: List[List[int]]) -> List[List[int]]:
    """
    Optimized approach by sorting intervals and merging in a single pass.
    Time complexity: O(N log N) dominated by the sort. The merge pass is O(N).
    Space complexity: O(N) if you count the output array, otherwise O(1) if modifying in-place
                      is allowed or if we don't count the output.
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Test cases
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
expected1 = [[1,6],[8,10],[15,18]]
assert merge_intervals_brute(intervals1) == expected1
assert merge_intervals_optimized(intervals1) == expected1

intervals2 = [[1,4],[4,5]]
expected2 = [[1,5]]
assert merge_intervals_brute(intervals2) == expected2
assert merge_intervals_optimized(intervals2) == expected2

intervals3 = [[1,4],[0,4]]
expected3 = [[0,4]]
assert merge_intervals_brute(intervals3) == expected3
assert merge_intervals_optimized(intervals3) == expected3

intervals4 = [[1,4],[2,3]]
expected4 = [[1,4]]
assert merge_intervals_brute(intervals4) == expected4
assert merge_intervals_optimized(intervals4) == expected4

print("All test cases passed!")

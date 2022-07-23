"""
13. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used
item before inserting a new item.

The operations must be done in O(1) average time complexity.
"""
import collections

# Brute force: Using a simple list or array.
# get(key): O(n) to search for the key.
# put(key, value): O(n) to search and O(n) to move elements if full.
# This would be highly inefficient.

# Optimized Solution using OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        # Move the key to the end to show it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Move the key to the end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # popitem(last=False) pops from the beginning (LRU)
            self.cache.popitem(last=False)

# Complexity Analysis
# Time Complexity: O(1) for both get and put. OrderedDict in Python is implemented
# using a hash table and a doubly linked list, providing O(1) for these operations.
# Space Complexity: O(capacity) to store the items in the cache.

# Test Cases
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1, "Test Case 1 Failed"
cache.put(3, 3) # evicts key 2
assert cache.get(2) == -1, "Test Case 2 Failed"
cache.put(4, 4) # evicts key 1
assert cache.get(1) == -1, "Test Case 3 Failed"
assert cache.get(3) == 3, "Test Case 4 Failed"
assert cache.get(4) == 4, "Test Case 5 Failed"

cache2 = LRUCache(1)
cache2.put(2, 1)
assert cache2.get(2) == 1, "Test Case 6 Failed"
cache2.put(3, 2)
assert cache2.get(2) == -1, "Test Case 7 Failed"
assert cache2.get(3) == 2, "Test Case 8 Failed"


print("All test cases pass")

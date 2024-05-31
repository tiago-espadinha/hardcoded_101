import collections
import threading
import time

class LRUCache:
    """
    A thread-safe LRU Cache with Time-To-Live (TTL) functionality.

    Entries are stored in an OrderedDict to maintain LRU order.
    A reentrant lock (RLock) is used to ensure thread safety for all cache operations.
    Each entry also stores its expiration time.
    """
    def __init__(self, capacity: int, ttl_seconds: int = 0):
        """
        Initializes the LRUCache.

        Args:
            capacity: The maximum number of items the cache can hold.
            ttl_seconds: Time in seconds after which an item expires.
                         If 0 or less, items do not expire based on time.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if ttl_seconds < 0:
            raise ValueError("TTL seconds cannot be negative.")

        self.capacity = capacity
        self.ttl_seconds = ttl_seconds
        self._cache = collections.OrderedDict()
        self._lock = threading.RLock() # Use RLock for potential re-entrancy if methods call each other

    def _is_expired(self, key: str) -> bool:
        """
        Checks if an entry for the given key has expired.
        Assumes the lock is already held.
        """
        if self.ttl_seconds <= 0:
            return False # TTL is not active

        _, expiry_time = self._cache[key]
        return expiry_time is not None and time.time() > expiry_time

    def get(self, key: str):
        """
        Retrieves an item from the cache.

        If the item is found and not expired, it's moved to the end (most recently used)
        and its value is returned. If expired or not found, None is returned.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if not found or expired.
        """
        with self._lock:
            if key not in self._cache:
                return None

            if self._is_expired(key):
                del self._cache[key]
                return None

            # Move the item to the end to mark it as most recently used
            value, expiry_time = self._cache.pop(key)
            self._cache[key] = (value, expiry_time)
            return value

    def put(self, key: str, value):
        """
        Inserts or updates an item in the cache.

        If the cache is at capacity and a new item is being added (or an existing one
        is updated, but its current position doesn't prevent eviction), the least
        recently used (first) item is removed.

        Args:
            key: The key of the item to insert/update.
            value: The value to associate with the key.
        """
        with self._lock:
            # Calculate new expiry time if TTL is active
            expiry_time = time.time() + self.ttl_seconds if self.ttl_seconds > 0 else None

            if key in self._cache:
                # If key exists, remove it first to update its position to the end
                # and refresh its value/expiry
                self._cache.pop(key)
            elif len(self._cache) >= self.capacity:
                # If cache is full, remove the least recently used item (first item)
                self._cache.popitem(last=False)

            self._cache[key] = (value, expiry_time)

    def size(self) -> int:
        """
        Returns the current number of items in the cache.
        """
        with self._lock:
            return len(self._cache)

    def clear(self):
        """
        Clears all items from the cache.
        """
        with self._lock:
            self._cache.clear()

    def __len__(self):
        return self.size()

    def __repr__(self):
        with self._lock:
            items = []
            for k, (v, exp) in self._cache.items():
                exp_str = f"expires={exp - time.time():.1f}s" if exp else "no_ttl"
                items.append(f"{k}:{v} ({exp_str})")
            return f"LRUCache(capacity={self.capacity}, ttl={self.ttl_seconds}s, current_size={len(self._cache)}, items=[{', '.join(items)}])"

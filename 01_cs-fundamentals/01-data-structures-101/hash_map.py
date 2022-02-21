from typing import Any, List, Optional, Tuple

class HashMap:
    def __init__(self, initial_capacity: int = 16):
        """
        Initialize a Hash Map with separate chaining.
        Args:
            initial_capacity (int): Starting number of buckets.
        """
        self.capacity = initial_capacity
        self.size = 0
        self.buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(self.capacity)]
        self.load_factor_threshold = 0.75

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    # O(1) avg, O(n) worst
    def set(self, key: Any, value: Any) -> None:
        """
        Insert or update a key-value pair.
        Args:
            key (Any): The key.
            value (Any): The value.
        Returns:
            None
        """
        if self.size / self.capacity >= self.load_factor_threshold:
            self._resize()

        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.size += 1

    # O(1) avg, O(n) worst
    def get(self, key: Any) -> Any:
        """
        Retrieve the value for a key.
        Args:
            key (Any): The key.
        Returns:
            Any: The value, or None if not found.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None

    # O(1) avg, O(n) worst
    def delete(self, key: Any) -> bool:
        """
        Remove a key-value pair.
        Args:
            key (Any): The key.
        Returns:
            bool: True if deleted, False otherwise.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def _resize(self) -> None:
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.set(key, value)

    # O(n)
    def keys(self) -> List[Any]:
        """
        Return a list of all keys in the hash map.
        Returns:
            List[Any]: All keys.
        """
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket:
                all_keys.append(key)
        return all_keys

    # O(n)
    def values(self) -> List[Any]:
        """
        Return a list of all values in the hash map.
        Returns:
            List[Any]: All values.
        """
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket:
                all_values.append(value)
        return all_values

    # O(n)
    def items(self) -> List[Tuple[Any, Any]]:
        """
        Return a list of all key-value pairs.
        Returns:
            List[Tuple]: All pairs.
        """
        all_items = []
        for bucket in self.buckets:
            for key, value in bucket:
                all_items.append((key, value))
        return all_items

    def __len__(self) -> int:
        """
        Return the number of key-value pairs.
        Returns:
            int: The size.
        """
        return self.size

    def __contains__(self, key: Any) -> bool:
        """
        Check if a key exists in the hash map.
        Args:
            key (Any): The key.
        Returns:
            bool: True if key exists.
        """
        return self.get(key) is not None

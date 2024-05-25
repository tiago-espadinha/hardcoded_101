import hashlib
import math

class BloomFilter:
    def __init__(self, capacity, error_rate):
        """
        :param capacity: Expected number of items to be stored.
        :param error_rate: Acceptable false positive rate (e.g., 0.05).
        """
        self.capacity = capacity
        self.error_rate = error_rate
        
        # Calculate size of bit array (m)
        self.size = self._get_size(capacity, error_rate)
        
        # Calculate number of hash functions (k)
        self.hash_count = self._get_hash_count(self.size, capacity)
        
        # Initialize bit array
        self.bit_array = [0] * self.size
        print(f"Bloom Filter initialized with size={self.size} and hash_count={self.hash_count}")

    def _get_size(self, n, p):
        """Calculate bit array size m."""
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    def _get_hash_count(self, m, n):
        """Calculate number of hash functions k."""
        k = (m / n) * math.log(2)
        return int(k)

    def _hashes(self, item):
        """Generate k hash indices for the given item."""
        indices = []
        for i in range(self.hash_count):
            # Use hashlib to generate unique hashes by salting the input
            # In a real system, you'd use a faster hash like Murmur3
            hash_hex = hashlib.sha256(f"{i}:{item}".encode()).hexdigest()
            index = int(hash_hex, 16) % self.size
            indices.append(index)
        return indices

    def add(self, item):
        for index in self._hashes(item):
            self.bit_array[index] = 1

    def might_contain(self, item):
        for index in self._hashes(item):
            if self.bit_array[index] == 0:
                return False
        return True

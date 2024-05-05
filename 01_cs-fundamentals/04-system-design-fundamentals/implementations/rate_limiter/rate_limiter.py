import threading
import time
import collections

class TokenBucketLimiter:
    """
    A thread-safe rate limiter based on the Token Bucket algorithm.

    Tokens are refilled at a fixed rate, up to a maximum capacity.
    Each request consumes one token. If no tokens are available, the request is denied.
    """
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initializes the TokenBucketLimiter.

        Args:
            capacity: The maximum number of tokens the bucket can hold.
            refill_rate: The rate at which tokens are refilled per second.
                         e.g., 10 means 10 tokens per second.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if refill_rate <= 0:
            raise ValueError("Refill rate must be a positive number.")

        self.capacity = capacity
        self.refill_rate = refill_rate
        self._tokens = capacity  # Current number of tokens in the bucket
        self._last_refill_time = time.monotonic()  # Last time tokens were refilled
        self._lock = threading.Lock()

    def _refill_tokens(self):
        """
        Calculates and adds tokens to the bucket based on elapsed time since last refill.
        Assumes the lock is already held.
        """
        now = time.monotonic()
        elapsed_time = now - self._last_refill_time
        tokens_to_add = elapsed_time * self.refill_rate
        self._tokens = min(self.capacity, self._tokens + tokens_to_add)
        self._last_refill_time = now

    def allow(self, key: str = None) -> bool:
        """
        Checks if a request is allowed.

        A token is consumed if available. If not, the request is denied.
        The 'key' parameter is included for API consistency with SlidingWindowLimiter,
        but it's not used in the Token Bucket algorithm itself (it's a global limit).

        Args:
            key: An optional identifier for the client (not used in this implementation).

        Returns:
            True if the request is allowed, False otherwise.
        """
        with self._lock:
            self._refill_tokens()
            if self._tokens >= 1:
                self._tokens -= 1
                return True
            return False

class SlidingWindowLimiter:
    """
    A thread-safe rate limiter based on the Sliding Window Log algorithm.

    This algorithm keeps a log of request timestamps within a defined window.
    When a new request arrives, it removes old timestamps and checks if the
    number of remaining timestamps (requests) exceeds the limit.
    """
    def __init__(self, limit: int, window_seconds: int):
        """
        Initializes the SlidingWindowLimiter.

        Args:
            limit: The maximum number of requests allowed within the window.
            window_seconds: The size of the sliding window in seconds.
        """
        if limit <= 0:
            raise ValueError("Limit must be a positive integer.")
        if window_seconds <= 0:
            raise ValueError("Window seconds must be a positive number.")

        self.limit = limit
        self.window_seconds = window_seconds
        # Using a defaultdict to store request timestamps for each key (client)
        # Each value is a deque, efficiently managing timestamps for the sliding window.
        self._request_logs = collections.defaultdict(collections.deque)
        self._lock = threading.Lock()

    def allow(self, key: str) -> bool:
        """
        Checks if a request from a specific key (client) is allowed.

        Args:
            key: A unique identifier for the client making the request.

        Returns:
            True if the request is allowed, False otherwise.
        """
        if not key:
            raise ValueError("A key must be provided for SlidingWindowLimiter.")

        with self._lock:
            now = time.monotonic()
            timestamps = self._request_logs[key]

            # Remove timestamps older than the current window
            while timestamps and timestamps[0] <= now - self.window_seconds:
                timestamps.popleft()

            # Check if adding the current request exceeds the limit
            if len(timestamps) < self.limit:
                timestamps.append(now)
                return True
            return False

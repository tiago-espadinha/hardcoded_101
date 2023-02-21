import time
from abc import ABC, abstractmethod
from typing import Dict, Tuple

class AbstractAPI(ABC):
    @abstractmethod
    def get_data(self, endpoint: str) -> str:
        pass

class RealAPI(AbstractAPI):
    """The real service that performs expensive network calls."""
    def get_data(self, endpoint: str) -> str:
        print(f"RealAPI: fetching data from {endpoint} (expensive operation)...")
        time.sleep(2)  # Simulate network latency
        return f"Data from {endpoint}"

class CachingProxy(AbstractAPI):
    """A proxy that caches responses from the RealAPI with a TTL."""
    
    def __init__(self, real_api: RealAPI, ttl: int = 5):
        self._real_api = real_api
        self._cache: Dict[str, Tuple[str, float]] = {}
        self._ttl = ttl

    def get_data(self, endpoint: str) -> str:
        now = time.time()
        
        if endpoint in self._cache:
            data, timestamp = self._cache[endpoint]
            if now - timestamp < self._ttl:
                print(f"CachingProxy: returning cached data for {endpoint}")
                return data
            else:
                print(f"CachingProxy: cache expired for {endpoint}")
        
        # If not in cache or expired, fetch from real subject
        data = self._real_api.get_data(endpoint)
        self._cache[endpoint] = (data, now)
        return data

if __name__ == "__main__":
    real_api = RealAPI()
    proxy = CachingProxy(real_api, ttl=3)
    
    # First call - expensive
    print(proxy.get_data("/users/1"))
    
    # Second call - fast (cached)
    print(proxy.get_data("/users/1"))
    
    # Wait for TTL to expire
    print("Waiting for cache to expire...")
    time.sleep(4)
    
    # Third call - expensive again
    print(proxy.get_data("/users/1"))

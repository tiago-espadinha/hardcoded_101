from pattern import RealAPI, CachingProxy
import time

class WeatherStationService:
    """A real-world service that uses a proxy to cache expensive weather API calls."""
    
    def __init__(self):
        # The proxy hides the real API and adds caching logic
        self.api = CachingProxy(RealAPI(), ttl=10)
        
    def show_weather(self, city: str):
        print(f"\n--- Checking weather for {city} ---")
        start = time.perf_counter()
        data = self.api.get_data(f"/weather/{city}")
        end = time.perf_counter()
        
        print(f"Weather: {data} (Took {end-start:.2f} seconds)")

if __name__ == "__main__":
    service = WeatherStationService()
    
    service.show_weather("New York")
    service.show_weather("London")
    service.show_weather("New York") # This should be cached and fast
    
    print("\nWaiting 11 seconds for cache to expire...")
    time.sleep(11)
    
    service.show_weather("New York") # This should be expensive again

import time
import random
from pattern import log_call, time_execution, retry

class DataIngestionService:
    """A service that simulates fetching data from a remote unreliable source."""
    
    @log_call
    @time_execution
    @retry(retries=3, delay=0.5)
    def fetch_user_data(self, user_id: int):
        print(f"--- Fetching data for user {user_id} ---")
        
        # Simulate network latency
        time.sleep(random.uniform(0.1, 0.4))
        
        # Simulate occasional network errors
        if random.random() < 0.3:
            raise ConnectionError("Temporary network failure!")
        
        return {
            "id": user_id,
            "name": f"User {user_id}",
            "last_active": "2023-02-15"
        }

if __name__ == "__main__":
    service = DataIngestionService()
    
    # Successful case (likely)
    try:
        data = service.fetch_user_data(101)
        print(f"Data received: {data}")
    except Exception as e:
        print(f"Service failed: {e}")
        
    # Another call
    try:
        data = service.fetch_user_data(202)
        print(f"Data received: {data}")
    except Exception as e:
        print(f"Service failed: {e}")

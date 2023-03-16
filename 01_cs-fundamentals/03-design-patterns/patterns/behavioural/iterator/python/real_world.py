from pattern import PaginatedAPIResponse
import time

class APIClient:
    """A client that fetches users across multiple pages."""
    
    def fetch_all_users(self):
        print("APIClient: Fetching users...")
        # Simulating data that arrived in chunks
        pages = [
            [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
            [{"id": 3, "name": "Charlie"}, {"id": 4, "name": "Dave"}],
            [{"id": 5, "name": "Eve"}]
        ]
        return PaginatedAPIResponse(pages)

if __name__ == "__main__":
    client = APIClient()
    users_iterable = client.fetch_all_users()
    
    print("\n--- User Directory ---")
    for user in users_iterable:
        print(f"[{user['id']}] {user['name']}")
        time.sleep(0.1)
    print("----------------------")

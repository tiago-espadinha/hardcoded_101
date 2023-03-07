from typing import List, Any

class PaginatedAPIResponse:
    """A custom iterable for paginated API responses."""
    
    def __init__(self, pages: List[List[Any]]):
        self._pages = pages
        self._current_page_idx = 0
        self._current_item_idx = 0

    def __iter__(self):
        """Returns the iterator object itself."""
        self._current_page_idx = 0
        self._current_item_idx = 0
        return self

    def __next__(self):
        """Returns the next item in the collection across all pages."""
        if self._current_page_idx >= len(self._pages):
            raise StopIteration

        page = self._pages[self._current_page_idx]
        
        if self._current_item_idx < len(page):
            item = page[self._current_item_idx]
            self._current_item_idx += 1
            return item
        else:
            # Move to next page
            self._current_page_idx += 1
            self._current_item_idx = 0
            return self.__next__()

if __name__ == "__main__":
    # Simulating 3 pages of results from an API
    api_data = [
        ["User 1", "User 2", "User 3"],
        ["User 4", "User 5"],
        ["User 6", "User 7", "User 8", "User 9"]
    ]
    
    paginated_response = PaginatedAPIResponse(api_data)
    
    print("Iterating through paginated response:")
    for user in paginated_response:
        print(f"Found: {user}")

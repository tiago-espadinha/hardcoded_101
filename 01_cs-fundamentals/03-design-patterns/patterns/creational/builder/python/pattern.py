from typing import Dict, Any, Optional

class HTTPRequest:
    def __init__(self, method: str, url: str):
        self.method = method
        self.url = url
        self.headers: Dict[str, str] = {}
        self.params: Dict[str, str] = {}
        self.body: Optional[str] = None

    def __str__(self):
        return f"HTTPRequest({self.method} {self.url}, Headers: {self.headers}, Params: {self.params}, Body: {self.body})"

class HTTPRequestBuilder:
    """Builder for HTTPRequest with method chaining."""
    def __init__(self, url: str):
        self._request = HTTPRequest("GET", url)

    def set_method(self, method: str) -> 'HTTPRequestBuilder':
        self._request.method = method.upper()
        return self

    def add_header(self, key: str, value: str) -> 'HTTPRequestBuilder':
        self._request.headers[key] = value
        return self

    def add_param(self, key: str, value: str) -> 'HTTPRequestBuilder':
        self._request.params[key] = value
        return self

    def set_body(self, body: str) -> 'HTTPRequestBuilder':
        self._request.body = body
        return self

    def build(self) -> HTTPRequest:
        return self._request

if __name__ == "__main__":
    builder = HTTPRequestBuilder("https://api.example.com")
    request = (
        builder.set_method("POST")
        .add_header("Content-Type", "application/json")
        .add_param("user_id", "123")
        .set_body('{"name": "Alice"}')
        .build()
    )
    print(f"Built Request: {request}")

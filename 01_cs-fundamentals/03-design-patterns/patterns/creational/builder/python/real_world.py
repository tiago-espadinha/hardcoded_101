from pattern import HTTPRequestBuilder

def fetch_data_from_api():
    """Demonstrates using the HTTPRequestBuilder to construct a complex request."""
    request = (
        HTTPRequestBuilder("https://api.example.com/v1/users")
        .set_method("POST")
        .add_header("Authorization", "Bearer my-secret-token")
        .add_header("Content-Type", "application/json")
        .add_param("debug", "true")
        .set_body('{"name": "John Doe", "email": "john@example.com"}')
        .build()
    )
    
    print(f"Executing request: {request}")

if __name__ == "__main__":
    fetch_data_from_api()

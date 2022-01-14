"""
Demonstrates Error Handling in Python.
Covers: try/except/else/finally, raising exceptions, custom exceptions,
        context managers with __enter__/__exit__
"""
import os

class FileProcessingError(Exception):
    """Custom exception for file processing issues."""
    pass

class MyContextManager:
    """A sample custom context manager."""
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        if exc_type:
            print(f"Exception caught in context: {exc_val}")
        return True # Suppress exception

def read_file_safely(file_path):
    """Exercise: robust file reader."""
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{file_path}'.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{file_path}' as text.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise FileProcessingError(f"Failed to process {file_path}") from e
    finally:
        print("Completed safety check.")

def main():
    # Context manager demo
    with MyContextManager():
        print("Inside context")
        # raise ValueError("Oops")

    # Error handling demo
    print(read_file_safely("nonexistent.txt"))
    
    # Try/except/else/finally demo
    try:
        num = int("123")
    except ValueError:
        print("Conversion failed")
    else:
        print(f"Converted number: {num}")
    finally:
        print("Conversion attempt finished")

if __name__ == "__main__":
    main()

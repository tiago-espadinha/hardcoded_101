import time
from functools import wraps
from typing import Callable, Any

def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that prints the function name and its elapsed time."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[{func.__name__}] Elapsed time: {elapsed:.6f} seconds")
        return result
    return wrapper

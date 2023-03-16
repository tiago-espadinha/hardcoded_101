import functools
import time
import logging
from typing import Callable, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def log_call(func: Callable) -> Callable:
    """Decorator that logs the function call and its result."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

def time_execution(func: Callable) -> Callable:
    """Decorator that measures and logs the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def retry(retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator that retries a function if it raises an exception."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1}/{retries} failed for {func.__name__}: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay)
            logger.error(f"All {retries} attempts failed for {func.__name__}")
            raise last_exception # type: ignore
        return wrapper
    return decorator

if __name__ == "__main__":
    @log_call
    @time_execution
    def say_hello(name: str) -> str:
        time.sleep(0.1)
        return f"Hello, {name}!"

    say_hello("World")

    @retry(retries=3, delay=0.1)
    def unstable_operation():
        import random
        if random.random() < 0.7:
            raise ValueError("Random failure!")
        return "Success!"

    try:
        print(unstable_operation())
    except ValueError:
        print("Operation failed after retries.")

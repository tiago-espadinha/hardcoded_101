"""
Demonstrates functions in Python.
Covers: def, return, default args, *args, **kwargs, type hints,
        docstrings, lambda, higher-order functions (map, filter, sorted)
"""
import time
from functools import wraps

def timer(func):
    """Function decorator that prints execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def heavy_computation(n: int, multiplier: int = 1) -> int:
    """A sample function to demonstrate decorator and type hints."""
    result = 0
    for i in range(n):
        result += i * multiplier
    return result

def var_args_demo(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

def main():
    print(f"Result: {heavy_computation(1_000_000, multiplier=2)}")
    
    var_args_demo(1, 2, 3, a="apple", b="banana")

    # Higher order functions
    nums = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, nums))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    sorted_data = sorted([("b", 2), ("a", 10), ("c", 1)], key=lambda x: x[1])

    print(f"Squared: {squared}")
    print(f"Evens: {evens}")
    print(f"Sorted data: {sorted_data}")

if __name__ == "__main__":
    main()

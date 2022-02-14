"""
Demonstrates functools in Python.
Covers: lru_cache, partial, reduce, wraps
"""
from functools import lru_cache, partial, reduce, wraps

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

def main():
    # lru_cache
    print(f"Fib(30): {fib(30)}")
    print(f"Cache stats: {fib.cache_info()}")

    # partial
    base2 = partial(int, base=2)
    print(f"Binary 101: {base2('101')}")

    # reduce
    nums = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, nums)
    print(f"Reduce total: {total}")

if __name__ == "__main__":
    main()

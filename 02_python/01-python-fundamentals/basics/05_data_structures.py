"""
Demonstrates data structures in Python.
Covers: list, tuple, dict, set, frozenset, comprehensions, slicing, unpacking, walrus operator
"""
from collections import Counter

def word_frequency_counter(text: str) -> dict[str, int]:
    """Word frequency counter using a dict."""
    words = text.lower().split()
    freq = {}
    for word in words:
        # Using walrus operator
        if (count := freq.get(word, 0)) >= 0:
            freq[word] = count + 1
    return freq

def main():
    # List and slicing
    nums = list(range(10))
    print(f"First 3: {nums[:3]}")
    print(f"Last 2: {nums[-2:]}")
    print(f"Stride 2: {nums[::2]}")

    # Unpacking
    a, b, *rest = nums
    print(f"a={a}, b={b}, rest={rest}")

    # Comprehensions
    squares = [x**2 for x in range(5)]
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    unique_chars = {c for c in "abracadabra"}
    print(f"Squares: {squares}")
    print(f"Even squares: {even_squares}")
    print(f"Unique: {unique_chars}")

    # Set and frozenset
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    print(f"Union: {s1 | s2}")
    print(f"Intersection: {s1 & s2}")
    fs = frozenset([1, 2, 3])
    # fs.add(4) # AttributeError

    # Exercise: word frequency
    sample_text = "The quick brown fox jumps over the lazy dog"
    print(f"Word frequency: {word_frequency_counter(sample_text)}")

if __name__ == "__main__":
    main()

"""
Demonstrates itertools in Python.
Covers: chain, product, combinations, permutations, groupby
"""
import itertools

def main():
    # chain
    print(f"Chain: {list(itertools.chain([1, 2], [3, 4]))}")

    # product
    print(f"Product: {list(itertools.product('AB', range(2)))}")

    # combinations and permutations
    print(f"Permutations AB: {list(itertools.permutations('AB'))}")
    print(f"Combinations ABC (2): {list(itertools.combinations('ABC', 2))}")

    # groupby
    data = sorted([("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")])
    for key, group in itertools.groupby(data, key=lambda x: x[0]):
        print(f"{key}: {list(group)}")

if __name__ == "__main__":
    main()

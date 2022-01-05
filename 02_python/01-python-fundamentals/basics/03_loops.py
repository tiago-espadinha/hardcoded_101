"""
Demonstrates loops in Python.
Covers: for, while, enumerate, zip, range, break, continue, else clause
"""

def prime_sieve(n):
    """Prime sieve up to N using nested loops."""
    primes = []
    is_prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return primes

def main():
    # Demonstrating various loop utilities
    items = ["apple", "banana", "cherry"]
    for index, value in enumerate(items):
        print(f"{index}: {value}")

    prices = [1.2, 0.5, 2.0]
    for item, price in zip(items, prices):
        print(f"{item} costs {price}")

    # While loop with break/continue
    count = 0
    while count < 10:
        count += 1
        if count % 2 == 0:
            continue
        if count > 7:
            break
        print(f"Odd count: {count}")
    else:
        print("Loop finished normally") # Won't print due to break

    print(f"Primes up to 50: {prime_sieve(50)}")

if __name__ == "__main__":
    main()

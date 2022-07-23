from typing import Dict

# Recurrence Relation: F(n) = F(n-1) + F(n-2)
# Base Cases: F(0) = 0, F(1) = 1

def fib_naive(n: int) -> int:
    """O(2^n) time, O(n) space."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n: int, memo: Dict[int, int] = None) -> int:
    """O(n) time, O(n) space."""
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def fib_tabulation(n: int) -> int:
    """O(n) time, O(n) space."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    print(f"DP Table: {dp}")
    return dp[n]

def fib_optimized(n: int) -> int:
    """O(n) time, O(1) space."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = 10
    print(f"Calculating Fib({n}):")
    print(f"Naive:     {fib_naive(n)}")
    print(f"Memo:      {fib_memo(n)}")
    print(f"Tabulation: {fib_tabulation(n)}")
    print(f"Optimized:  {fib_optimized(n)}")

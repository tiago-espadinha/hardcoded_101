"""
You are given an integer array `coins` representing coins of different
denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import List
import sys

# Brute-force solution (Recursion)
def coin_change_brute(coins: List[int], amount: int) -> int:
    """
    Brute-force recursive solution.
    Time complexity: O(C^A), where C is the number of coins and A is the amount.
                     Exponential because of the branching factor.
    Space complexity: O(A) for the recursion depth.
    """
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    min_coins = float('inf')

    for coin in coins:
        result = coin_change_brute(coins, amount - coin)
        if result != -1:
            min_coins = min(min_coins, result + 1)

    return min_coins if min_coins != float('inf') else -1

# Optimized solution (Dynamic Programming)
def coin_change_optimized(coins: List[int], amount: int) -> int:
    """
    Optimized solution using bottom-up Dynamic Programming.
    Time complexity: O(A * C), where A is the amount and C is the number of coins.
                     We iterate through each amount up to A, and for each, we check each coin.
    Space complexity: O(A) for the DP table.
    """
    # dp[i] will be storing the minimum number of coins required for amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Test cases
coins1 = [1, 2, 5]
amount1 = 11
# Expected: 3 (5 + 5 + 1)
# Note: The brute-force solution can be very slow for larger inputs.
# We will test it with a smaller amount.
assert coin_change_brute(coins1, 6) == 2 # 5 + 1
assert coin_change_optimized(coins1, 11) == 3

coins2 = [2]
amount2 = 3
# Expected: -1
assert coin_change_brute(coins2, amount2) == -1
assert coin_change_optimized(coins2, amount2) == -1

coins3 = [1]
amount3 = 0
# Expected: 0
assert coin_change_brute(coins3, amount3) == 0
assert coin_change_optimized(coins3, amount3) == 0

coins4 = [1]
amount4 = 2
# Expected: 2 (1+1)
assert coin_change_brute(coins4, amount4) == 2
assert coin_change_optimized(coins4, amount4) == 2


print("All test cases passed!")

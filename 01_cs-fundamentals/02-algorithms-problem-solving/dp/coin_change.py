from typing import List, Dict

# Recurrence Relation:
# dp[amount] = min(1 + dp[amount - coin]) for all coin in coins
# Base case: dp[0] = 0

def coin_change_top_down(coins: List[int], amount: int) -> int:
    """O(n*amount) time, O(amount) space."""
    memo: Dict[int, int] = {0: 0}

    def solve(rem: int) -> int:
        if rem < 0:
            return float('inf')
        if rem in memo:
            return memo[rem]
        
        min_coins = float('inf')
        for coin in coins:
            res = solve(rem - coin)
            if res != float('inf'):
                min_coins = min(min_coins, 1 + res)
        
        memo[rem] = min_coins
        return min_coins

    result = solve(amount)
    return result if result != float('inf') else -1

def coin_change_bottom_up(coins: List[int], amount: int) -> int:
    """O(n*amount) time, O(amount) space."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
                
    print(f"DP Table: {dp}")
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    
    print(f"Coins:  {coins}")
    print(f"Amount: {amount}")
    
    print(f"Min Coins (Top-Down):  {coin_change_top_down(coins, amount)}")
    print(f"Min Coins (Bottom-Up): {coin_change_bottom_up(coins, amount)}")

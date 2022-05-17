from typing import List, Dict, Tuple

# Recurrence Relation:
# dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1]) if w >= weights[i-1]
# else dp[i-1][w]
# Base case: dp[0][w] = 0, dp[i][0] = 0

def knapsack_top_down(weights: List[int], values: List[int], capacity: int) -> int:
    """O(n*W) time, O(n*W) space."""
    memo: Dict[Tuple[int, int], int] = {}

    def solve(n: int, cap: int) -> int:
        if n == 0 or cap == 0:
            return 0
        if (n, cap) in memo:
            return memo[(n, cap)]
        
        if weights[n-1] > cap:
            result = solve(n - 1, cap)
        else:
            result = max(
                solve(n - 1, cap),
                values[n - 1] + solve(n - 1, cap - weights[n - 1])
            )
        
        memo[(n, cap)] = result
        return result

    return solve(len(weights), capacity)

def knapsack_bottom_up(weights: List[int], values: List[int], capacity: int) -> int:
    """O(n*W) time, O(n*W) space."""
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    print("DP Table (Small Snippet):")
    for row in dp[:i+1]:
        print(row)
        
    return dp[n][capacity]

if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [60, 100, 120]
    capacity = 5
    
    print(f"Weights:  {weights}")
    print(f"Values:   {values}")
    print(f"Capacity: {capacity}")
    
    print(f"Max Value (Top-Down):  {knapsack_top_down(weights, values, capacity)}")
    print(f"Max Value (Bottom-Up): {knapsack_bottom_up(weights, values, capacity)}")

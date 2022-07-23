from typing import Dict

# Recurrence Relation:
# dp[n] = dp[n-1] + dp[n-2]
# Base cases: dp[1] = 1, dp[2] = 2

def climb_stairs_top_down(n: int) -> int:
    """O(n) time, O(n) space."""
    memo: Dict[int, int] = {1: 1, 2: 2}

    def solve(steps: int) -> int:
        if steps in memo:
            return memo[steps]
        memo[steps] = solve(steps - 1) + solve(steps - 2)
        return memo[steps]

    if n == 0: return 0
    return solve(n)

def climb_stairs_bottom_up(n: int) -> int:
    """O(n) time, O(n) space."""
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    print(f"DP Table: {dp}")
    return dp[n]

if __name__ == "__main__":
    n = 5
    print(f"Number of steps: {n}")
    print(f"Ways (Top-Down):  {climb_stairs_top_down(n)}")
    print(f"Ways (Bottom-Up): {climb_stairs_bottom_up(n)}")

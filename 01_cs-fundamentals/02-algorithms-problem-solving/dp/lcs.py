from typing import Dict, Tuple

# Recurrence Relation:
# if s1[i] == s2[j]: dp[i][j] = 1 + dp[i-1][j-1]
# else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# Base case: dp[0][j] = 0, dp[i][0] = 0

def lcs_top_down(s1: str, s2: str) -> int:
    """O(m*n) time, O(m*n) space."""
    memo: Dict[Tuple[int, int], int] = {}

    def solve(m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if (m, n) in memo:
            return memo[(m, n)]
        
        if s1[m-1] == s2[n-1]:
            result = 1 + solve(m - 1, n - 1)
        else:
            result = max(solve(m - 1, n), solve(m, n - 1))
            
        memo[(m, n)] = result
        return result

    return solve(len(s1), len(s2))

def lcs_bottom_up(s1: str, s2: str) -> Tuple[int, str]:
    """O(m*n) time, O(m*n) space."""
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Print table
    print("DP Table:")
    for row in dp:
        print(row)

    # Backtrack to find the LCS string
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_str.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return dp[m][n], "".join(reversed(lcs_str))

if __name__ == "__main__":
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    
    print(f"S1: {s1}, S2: {s2}")
    print(f"Length (Top-Down): {lcs_top_down(s1, s2)}")
    length, sequence = lcs_bottom_up(s1, s2)
    print(f"Length (Bottom-Up): {length}")
    print(f"Sequence: {sequence}")

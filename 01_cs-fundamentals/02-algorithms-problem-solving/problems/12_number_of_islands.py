"""
12. Number of Islands

Given a 2D grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
"""

# Brute-force is not really applicable here. The standard solution is already efficient.
# One could argue a less optimal approach would be one with higher space complexity,
# but the algorithmic approach (DFS/BFS) is standard.

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                num_islands += 1
                dfs(grid, i, j)
    return num_islands

def dfs(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
        return
    grid[r][c] = '0' # Mark as visited
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)

# Complexity Analysis
# Time Complexity: O(M*N), where M is the number of rows and N is the number of columns.
# We visit each cell once.
# Space Complexity: O(M*N) in the worst case (a grid full of '1's) for the recursion stack.
# Can be O(min(M,N)) if we use BFS with a queue.

# Test Cases
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
assert numIslands([row[:] for row in grid1]) == 1, "Test Case 1 Failed"

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
assert numIslands([row[:] for row in grid2]) == 3, "Test Case 2 Failed"

grid3 = [
    ["1","0","1","0","1"]
]
assert numIslands([row[:] for row in grid3]) == 3, "Test Case 3 Failed"

print("All test cases pass")

"""
11. Word Search

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where "adjacent"
cells are those horizontally or vertically neighboring. The same letter cell may not be
used more than once.
"""

# Brute Force: Not applicable in the same way as other problems, the standard solution
# is already a form of exhaustive search (DFS). A "more" brute-force way would be to
# generate all possible paths on the grid, which is computationally infeasible and overly complex.
# The standard DFS backtracking approach is the canonical way to solve this.

# Optimized Solution (DFS / Backtracking)
def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if not board:
        return False
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0, board, word):
                return True
    return False

def backtrack(r, c, i, board, word):
    if i == len(word):
        return True
    rows, cols = len(board), len(board[0])
    if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
        return False

    # Mark the cell as visited
    temp = board[r][c]
    board[r][c] = "#"

    # Explore neighbors
    res = (backtrack(r + 1, c, i + 1, board, word) or
           backtrack(r - 1, c, i + 1, board, word) or
           backtrack(r, c + 1, i + 1, board, word) or
           backtrack(r, c - 1, i + 1, board, word))

    # Un-mark the cell
    board[r][c] = temp
    return res

# Complexity Analysis
# Time Complexity: O(N * 3^L) where N is the number of cells in the grid and L is the length of the word.
# For each cell, we initiate a DFS. The DFS can go in 3 directions at each step (can't go back).
# Space Complexity: O(L) for the recursion stack, where L is the length of the word.

# Test Cases
board1 = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word1 = "ABCCED"
assert exist([row[:] for row in board1], word1) == True, "Test Case 1 Failed"

board2 = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word2 = "SEE"
assert exist([row[:] for row in board2], word2) == True, "Test Case 2 Failed"

board3 = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word3 = "ABCB"
assert exist([row[:] for row in board3], word3) == False, "Test Case 3 Failed"

print("All test cases pass")

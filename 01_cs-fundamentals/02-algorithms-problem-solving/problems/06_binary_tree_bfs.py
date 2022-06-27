"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
"""
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Brute-force solution
def level_order_brute(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal using recursion.
    Time complexity: O(N), where N is the number of nodes. We visit each node once.
    Space complexity: O(H) for the recursion stack, where H is the height of the tree.
                      In the worst case (a skewed tree), this can be O(N).
    """
    if not root:
        return []

    result = []
    
    def traverse(node, level):
        if not node:
            return
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)

    traverse(root, 0)
    return result

# Optimized solution
def level_order_optimized(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal using a queue (BFS).
    Time complexity: O(N), where N is the number of nodes. We visit each node once.
    Space complexity: O(W), where W is the maximum width of the tree. In the worst case
                      (a complete binary tree), the last level can contain up to N/2 nodes,
                      so space complexity is O(N).
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result

# Test cases
# Tree 1: [3,9,20,null,null,15,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
assert level_order_brute(root1) == [[3], [9, 20], [15, 7]]
assert level_order_optimized(root1) == [[3], [9, 20], [15, 7]]

# Tree 2: [1]
root2 = TreeNode(1)
assert level_order_brute(root2) == [[1]]
assert level_order_optimized(root2) == [[1]]

# Tree 3: []
root3 = None
assert level_order_brute(root3) == []
assert level_order_optimized(root3) == []

# Tree 4: [1,2,3,4,5]
root4 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
assert level_order_brute(root4) == [[1], [2, 3], [4, 5]]
assert level_order_optimized(root4) == [[1], [2, 3], [4, 5]]

print("All test cases passed!")

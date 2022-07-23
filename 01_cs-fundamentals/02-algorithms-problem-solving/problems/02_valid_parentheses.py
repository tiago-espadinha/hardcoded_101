"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

def is_valid_brute_force(s: str) -> bool:
    """
    This problem doesn't have a typical 'brute-force' solution that is much less efficient in terms of time complexity
    than the optimal one. The stack-based approach is the standard and most intuitive way to solve this.
    For the sake of providing an alternative, one might think of a solution involving repeated string replacements,
    but this is generally less efficient and can be more complex to implement correctly.

    A stack-based approach is both the 'brute-force' in a sense and the optimal solution.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    return is_valid_optimized(s)


def is_valid_optimized(s: str) -> bool:
    """
    Optimized solution using a stack.
    Time complexity: O(n)
    Space complexity: O(n) in the worst case (all opening brackets).
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# Test cases
assert is_valid_optimized("()") is True
assert is_valid_optimized("()[]{}") is True
assert is_valid_optimized("(]") is False
assert is_valid_optimized("([)]") is False
assert is_valid_optimized("{[]}") is True
assert is_valid_optimized("") is True
assert is_valid_optimized("(") is False
assert is_valid_optimized(")") is False

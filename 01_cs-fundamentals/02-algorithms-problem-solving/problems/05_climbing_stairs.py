"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def climb_stairs_brute_force(n: int) -> int:
    """
    Brute force solution using recursion.
    This is very slow because it re-computes the same subproblems many times.
    Time complexity: O(2^n) - Exponential, as each call branches into two more calls.
    Space complexity: O(n) - For the recursion stack depth.
    """
    if n <= 2:
        return n
    return climb_stairs_brute_force(n - 1) + climb_stairs_brute_force(n - 2)


def climb_stairs_optimized(n: int) -> int:
    """
    Optimized solution using Dynamic Programming.
    This is essentially calculating the nth Fibonacci number.
    We can optimize space by only storing the last two values.
    Time complexity: O(n) - A single loop up to n.
    Space complexity: O(1) - We only use two variables to store the previous two results.
    """
    if n <= 2:
        return n
    
    one_step_before = 2
    two_steps_before = 1
    
    for _ in range(3, n + 1):
        all_ways = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = all_ways
        
    return one_step_before

# Test cases
# Brute Force
assert climb_stairs_brute_force(2) == 2
assert climb_stairs_brute_force(3) == 3
assert climb_stairs_brute_force(4) == 5

# Optimized
assert climb_stairs_optimized(2) == 2
assert climb_stairs_optimized(3) == 3
assert climb_stairs_optimized(5) == 8
assert climb_stairs_optimized(1) == 1

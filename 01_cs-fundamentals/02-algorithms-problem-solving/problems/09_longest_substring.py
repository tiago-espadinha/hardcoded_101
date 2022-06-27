"""
Given a string `s`, find the length of the longest substring without repeating
characters.
"""

# Brute-force solution
def length_of_longest_substring_brute(s: str) -> int:
    """
    Brute-force solution by checking all possible substrings.
    Time complexity: O(N^3), where N is the length of the string.
                     O(N^2) for generating substrings, and O(N) for checking for duplicates.
    Space complexity: O(K) where K is the size of the character set (or min(N, K)).
    """
    n = len(s)
    if n == 0:
        return 0
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if len(set(substring)) == len(substring):
                max_len = max(max_len, len(substring))
    return max_len

# Optimized solution (Sliding Window)
def length_of_longest_substring_optimized(s: str) -> int:
    """
    Optimized solution using the sliding window technique.
    Time complexity: O(N), where N is the length of the string. Each character is
                     visited at most twice (by the left and right pointers).
    Space complexity: O(K), where K is the size of the character set.
                      We use a hash map to store characters in the current window.
    """
    n = len(s)
    max_len = 0
    start = 0
    char_map = {} # Stores the last seen index of a character
    
    for end in range(n):
        if s[end] in char_map and char_map[s[end]] >= start:
            # If the character is already in the current window,
            # move the start of the window to the right of the last occurrence.
            start = char_map[s[end]] + 1
        
        # Update the last seen index of the character
        char_map[s[end]] = end
        
        # Update the maximum length found so far
        max_len = max(max_len, end - start + 1)
        
    return max_len

# Test cases
s1 = "abcabcbb"
assert length_of_longest_substring_brute(s1) == 3
assert length_of_longest_substring_optimized(s1) == 3

s2 = "bbbbb"
assert length_of_longest_substring_brute(s2) == 1
assert length_of_longest_substring_optimized(s2) == 1

s3 = "pwwkew"
# "wke" is the longest substring
assert length_of_longest_substring_brute(s3) == 3
assert length_of_longest_substring_optimized(s3) == 3

s4 = " "
assert length_of_longest_substring_brute(s4) == 1
assert length_of_longest_substring_optimized(s4) == 1

s5 = "dvdf"
# "vdf" is the longest substring
assert length_of_longest_substring_brute(s5) == 3
assert length_of_longest_substring_optimized(s5) == 3

print("All test cases passed!")

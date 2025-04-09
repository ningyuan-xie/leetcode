"""394. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Description: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions of
the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not)."""


class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize two pointers to traverse the strings s and t
        i, j = 0, 0
        # Traverse the strings s and t to check if s is a subsequence of t
        while i < len(s) and j < len(t):
            # If the characters in s and t are the same, move the pointer in s
            if s[i] == t[j]:
                i += 1
            # Move the pointer in t to check the next character
            j += 1
        # If the pointer in s reaches the end, return True
        return i == len(s)


# Input: s = "abc", t = "ahbgdc", Output: True
assert Solution.isSubsequence("abc", "ahbgdc") is True

# Input: s = "axc", t = "ahbgdc", Output: False
assert Solution.isSubsequence("axc", "ahbgdc") is False

print("All unit tests are passed.")

"""394. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Description: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not)."""


class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n + m), Space Complexity: O(1)."""
        # Initialize two pointers for s and t
        s_pointer, t_pointer = 0, 0

        # Iterate through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If characters match, move the pointer in s
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Always move the pointer in t
            t_pointer += 1

        # If we have traversed all characters in s, it is a subsequence of t
        return s_pointer == len(s)


def unit_tests():
    # Input: s = "abc", t = "ahbgdc", Output: True
    assert Solution.isSubsequence("abc", "ahbgdc") is True

    # Input: s = "axc", t = "ahbgdc", Output: False
    assert Solution.isSubsequence("axc", "ahbgdc") is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""521. Longest Uncommon Subsequence I
Link: https://leetcode.com/problems/longest-uncommon-subsequence-i/
Difficulty: Easy
Description: Given two strings a and b, return the length of the longest uncommon
subsequence between a and b. If no such uncommon subsequence exists, return -1.
An uncommon subsequence between two strings is a string that is a subsequence of
exactly one of them."""


class Solution:
    @staticmethod
    def findLUSlength(a: str, b: str) -> int:
        """Optimal Solution: Compare the two strings.
           Time Complexity: O(1), Space Complexity: O(1)"""
        # Return the length of the longest uncommon subsequence
        # If a is not equal to b, return the maximum length of a and b
        return max(len(a), len(b)) if a != b else -1


# Unit Test: Input = "aba", "cdc", Output = 3
assert Solution.findLUSlength("aba", "cdc") == 3

# Unit Test: Input = "aaa", "aaa", Output = -1
assert Solution.findLUSlength("aaa", "aaa") == -1

# Unit Test: Input = "aefawfawfawfaw", "aefawfeawfwafwaef", Output = 17
assert Solution.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef") == 17

print("All unit tests are passed")

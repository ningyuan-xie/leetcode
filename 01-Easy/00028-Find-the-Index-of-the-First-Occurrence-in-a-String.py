"""28. Find the Index of the First Occurrence in a String
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy
Description: Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack."""


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)"""
        # If needle is empty, return 0
        if not needle:
            return 0
        # Loop through the index of characters in the haystack
        for i in range(len(haystack) + 1 - len(needle)):  # E.g. "hello" and "ll": i = 0, 1, 2, 3
            # If the needle is part of the haystack, return the index
            if haystack[i: i + len(needle)] == needle:
                return i
        # If the needle is not part of the haystack, return -1
        return -1


# Input: haystack = "hello", needle = "ll", Output: 2
assert Solution.strStr("hello", "ll") == 2

# Input: haystack = "hello", needle = "lll", Output: -1
assert Solution.strStr("hello", "lll") == -1

# Input: haystack = "aaaaa", needle = "bba", Output: -1
assert Solution.strStr("aaaaa", "bba") == -1

# Input: haystack = "", needle = "", Output: 0
assert Solution.strStr("", "") == 0

print("All unit tests are passed.")

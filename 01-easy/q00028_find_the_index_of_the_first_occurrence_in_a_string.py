"""28. Find the Index of the First Occurrence in a String
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy
Description: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        # Loop through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # If the substring of haystack matches the needle, return the index
            if haystack[i:i + len(needle)] == needle:
                return i

        # If no match is found, return -1
        return -1


def unit_tests():
    # Input: haystack = "sadbutsad", needle = "sad", Output: 0
    assert Solution.strStr("sadbutsad", "sad") == 0

    # Input: haystack = "hello", needle = "ll", Output: 2
    assert Solution.strStr("hello", "ll") == 2

    # Input: haystack = "hello", needle = "lll", Output: -1
    assert Solution.strStr("hello", "lll") == -1

    # Input: haystack = "aaaaa", needle = "bba", Output: -1
    assert Solution.strStr("aaaaa", "bba") == -1

    # Input: haystack = "", needle = "", Output: 0
    assert Solution.strStr("", "") == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

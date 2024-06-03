# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy
# Description: Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        # If needle is empty, return 0
        if not needle:
            return 0
        # Loop through the index of characters in the haystack
        for i in range(len(haystack)):
            # Loop through the index of characters in the needle
            for j in range(len(needle)):
                # If the current index i + j is out of range of the haystack,
                # or the current character in the haystack does not match the character in the needle,
                # break out of the loop
                if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                    break
                # If the current index j is at the end of the needle,
                # return the index i of the first occurrence of the needle in the haystack
                if j == len(needle) - 1:
                    return i
        return -1


# Unit Test: Input: haystack = "hello", needle = "ll", Output: 2
assert Solution.strStr("hello", "ll") == 2

# Unit Test: Input: haystack = "aaaaa", needle = "bba", Output: -1
assert Solution.strStr("aaaaa", "bba") == -1

# Unit Test: Input: haystack = "", needle = "", Output: 0
assert Solution.strStr("", "") == 0
print("All unit tests are passed")

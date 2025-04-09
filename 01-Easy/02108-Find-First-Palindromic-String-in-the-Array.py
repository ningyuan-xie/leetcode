"""2108. Find First Palindromic String in the Array
Link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array
Difficulty: Easy
Description: Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward."""

from typing import List


class Solution:
    @staticmethod
    def firstPalindrome(words: List[str]) -> str:
        """Optimal Solution: Palindrome Check. Time Complexity: O(n), Space Complexity: O(1)"""

        def is_palindrome(s: str) -> bool:
            """Helper function to check if the string is palindrome"""
            return s == s[::-1]

        for word in words:
            if is_palindrome(word):
                return word
        return ""


# Unit Test: words = ["abc", "aba", "xyz", "aba"], Output: "aba"
assert Solution.firstPalindrome(["abc", "aba", "xyz", "aba"]) == "aba"

# Unit Test: words = ["notapalindrome","racecar"], Output: "racecar"
assert Solution.firstPalindrome(["notapalindrome", "racecar"]) == "racecar"

# Unit Test: words = ["def","ghi"], Output: ""
assert Solution.firstPalindrome(["def", "ghi"]) == ""

print("All unit tests are passed.")

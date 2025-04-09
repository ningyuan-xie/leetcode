"""680. Valid Palindrome II
Link: https://leetcode.com/problems/valid-palindrome-ii/
Difficulty: Easy
Description: Given a string s, return true if the s can be palindrome after deleting at most one
character from it."""


class Solution:
    @staticmethod
    def validPalindrome(s: str) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0125-Valid-Palindrome.py"""

        def is_palindrome(l: int, r: int) -> bool:
            """Helper function: Check if the substring s[left:right+1] is a palindrome"""
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # Initialize the two pointers
        left, right = 0, len(s) - 1

        # Check if the string s is a palindrome
        while left < right:
            if s[left] != s[right]:
                # Check if deleting one character makes the string a palindrome
                return (is_palindrome(left + 1, right)
                        or is_palindrome(left, right - 1))
            left += 1
            right -= 1
        return True


# Input: s = "aba", Output: True
assert Solution.validPalindrome("aba") is True

# Input: s = "abca", Output: True
assert Solution.validPalindrome("abca") is True

# Input: s = "abc", Output: False
assert Solution.validPalindrome("abc") is False

print("All unit tests are passed.")

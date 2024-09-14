"""9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Description: Given an integer x, return true if x is palindrome integer."""


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        """Optimal Solution: Convert to String. Time Complexity: O(n), Space Complexity: O(n).
           Alternative methods in 0344-Reverse-String.py: Two Pointers, Stack, Recursion"""
        # Convert integer to string
        x = str(x)
        # Compare string with reversed string
        return x == x[::-1]
        # start and stop are omitted,
        # so the slice starts from the beginning and goes to the end of the string
        # If step is set to -1, the slice goes from the end of the string to the beginning.


# Unit Test: Input: x = 121, Output: True
assert Solution.isPalindrome(121) is True

# Unit Test: Input: x = -121, Output: False
assert Solution.isPalindrome(-121) is False

# Unit Test: Input: x = 10, Output: False
assert Solution.isPalindrome(10) is False

print("All unit tests are passed")

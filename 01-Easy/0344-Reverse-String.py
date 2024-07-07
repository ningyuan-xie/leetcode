# Link: https://leetcode.com/problems/reverse-string/
# Difficulty: Easy
# Description: Write a function that reverses a string.
# The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List


class Solution:
    # Optimal Solution: Two-Pointers. Time Complexity: O(n), Space Complexity: O(1)
    # Similar to 0283-Move-Zeroes.py
    @staticmethod
    def reverseString(s: List[str]) -> None:
        # Initialize two pointers: left and right
        left, right = 0, len(s) - 1

        # Loop until left pointer is less than right pointer
        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the left pointer to the right
            left += 1
            # Move the right pointer to the left
            right -= 1


# Unit Test: Input: s = ["h", "e", "l", "l", "o"], Output: ["o", "l", "l", "e", "h"]
s_test = ["h", "e", "l", "l", "o"]
Solution.reverseString(s_test)
assert s_test == ["o", "l", "l", "e", "h"]

# Unit Test: Input: s = ["H", "a", "n", "n", "a", "h"], Output: ["h", "a", "n", "n", "a", "H"]
s_test = ["H", "a", "n", "n", "a", "h"]
Solution.reverseString(s_test)
assert s_test == ["h", "a", "n", "n", "a", "H"]

print("All unit tests are passed")

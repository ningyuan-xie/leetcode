"""344. Reverse String
Link: https://leetcode.com/problems/reverse-string/
Difficulty: Easy
Description: Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory."""

from typing import List


class Solution:
    @staticmethod
    def reverseString(s: List[str]) -> None:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize two pointers: left and right
        left, right = 0, len(s) - 1
        # Loop until left pointer >= right pointer
        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the left pointer to the right and the right pointer to the left
            left += 1
            right -= 1


def unit_tests():
    # Input: s = ["h", "e", "l", "l", "o"], Output: ["o", "l", "l", "e", "h"]
    s_test = ["h", "e", "l", "l", "o"]
    Solution.reverseString(s_test)
    assert s_test == ["o", "l", "l", "e", "h"]

    # Input: s = ["H", "a", "n", "n", "a", "h"], Output: ["h", "a", "n", "n", "a", "H"]
    s_test = ["H", "a", "n", "n", "a", "h"]
    Solution.reverseString(s_test)
    assert s_test == ["h", "a", "n", "n", "a", "H"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

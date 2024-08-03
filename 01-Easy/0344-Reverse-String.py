"""344. Reverse String
Link: https://leetcode.com/problems/reverse-string/
Difficulty: Easy
Description: Write a function that reverses a string.
The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory."""

from typing import List


class Solution:
    @staticmethod
    def reverseString(s: List[str]) -> None:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)
           Similar to 0283-Move-Zeroes.py"""
        # Initialize two pointers: left and right
        left, right = 0, len(s) - 1
        # Loop until left pointer >= right pointer
        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the left pointer to the right
            left += 1
            # Move the right pointer to the left
            right -= 1

    @staticmethod
    def reverseStringStack(s: List[str]) -> None:
        """Alternative Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)
           Similar to 0232-Implement-Queue-Using-Stacks.py"""
        # Initialize a stack to store the characters of s
        stack = []
        # Push each character of s into the stack
        for char in s:
            stack.append(char)
        # Pop each character from the stack and assign it to s
        for i in range(len(s)):
            s[i] = stack.pop()

    @staticmethod
    def reverseStringRecursion(s: List[str]) -> None:
        """Alternative Solution: Recursion. Time Complexity: O(n), Space Complexity: O(n)"""
        # Base case: if the length of s is less than or equal to 1, return
        if len(s) <= 1:
            return
        # Swap the first and last characters
        s[0], s[-1] = s[-1], s[0]
        # Recursively reverse the substring s[1:-1]
        Solution.reverseStringRecursion(s[1:-1])


# Unit Test: Input: s = ["h", "e", "l", "l", "o"], Output: ["o", "l", "l", "e", "h"]
s_test = ["h", "e", "l", "l", "o"]
Solution.reverseString(s_test)
assert s_test == ["o", "l", "l", "e", "h"]

# Unit Test: Input: s = ["H", "a", "n", "n", "a", "h"], Output: ["h", "a", "n", "n", "a", "H"]
s_test = ["H", "a", "n", "n", "a", "h"]
Solution.reverseStringRecursion(s_test)
assert s_test == ["h", "a", "n", "n", "a", "H"]

print("All unit tests are passed")

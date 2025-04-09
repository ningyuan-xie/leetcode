"""2235. Add Two Integers
Link: https://leetcode.com/problems/add-two-integers/
Difficulty: Easy
Description: Given two integers num1 and num2, return the sum of the two integers."""


class Solution:
    @staticmethod
    def sum(num1: int, num2: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)"""
        return num1 + num2


# Unit Test: num1 = 12, num2 = 5, Output: 17
assert Solution.sum(12, 5) == 17

# Unit Test: num1 = -10, num2 = 4, Output: -6
assert Solution.sum(-10, 4) == -6

print("All unit tests are passed.")

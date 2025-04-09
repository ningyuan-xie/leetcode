"""263. Ugly Number
Link: https://leetcode.com/problems/ugly-number/
Difficulty: Easy
Description: Write a program to check whether a given number is an ugly number.
An ugly number is a positive number whose prime factors only include 2, 3, and/or 5."""


class Solution:
    @staticmethod
    def isUgly(n: int) -> bool:
        """Optimal Solution: Iteration. Time Complexity: O(log(n)), Space Complexity: O(1)"""
        # Base case: if the number is less than or equal to 0, return False
        if n <= 0:
            return False

        # Check if the number is divisible by 2, 3, and 5
        for prime in [2, 3, 5]:
            while n % prime == 0:  # Divisible by prime
                n //= prime  # E.g., 6 // 2 = 3, 3 // 3 = 1; 8 // 2 = 4, 4 // 2 = 2, 2 // 2 = 1

        # If the number is an ugly number, the result should be 1
        return n == 1


# Input: num = 6, Output: True
assert Solution.isUgly(6) is True

# Input: num = 8, Output: True
assert Solution.isUgly(8) is True

# Input: num = 14, Output: False
assert Solution.isUgly(14) is False

print("All unit tests are passed.")

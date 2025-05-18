"""509. Fibonacci Number
Link: https://leetcode.com/problems/fibonacci-number/
Difficulty: Easy
Description: The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
• F(0) = 0, F(1) = 1
• F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n)."""


class Solution:
    @staticmethod
    def fib(n: int) -> int:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base cases
        if n <= 1:
            return n
        
        # Initialize the two variables
        one, two = 0, 1
        # F(n) = F(n-1) + F(n-2)
        for _ in range(n - 1):
            one, two = two, one + two
        return two


def unit_tests():
    # Input = 0, Output = 0
    assert Solution.fib(0) == 0

    # Input = 1, Output = 1
    assert Solution.fib(1) == 1

    # Input = 2, Output = 1
    assert Solution.fib(2) == 1

    # Input = 3, Output = 2
    assert Solution.fib(3) == 2

    # Input = 4, Output = 3
    assert Solution.fib(4) == 3


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

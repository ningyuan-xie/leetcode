"""509. Fibonacci Number
Link: https://leetcode.com/problems/fibonacci-number/
Difficulty: Easy
Description: The Fibonacci numbers, commonly denoted F(n) form a sequence, called
the Fibonacci sequence, such that each number is the sum of the two preceding ones,
starting from 0 and 1. That is, F(0) = 0, F(1) = 1, F(n) = F(n - 1) + F(n - 2) for n > 1.
Given n, calculate F(n)."""


class Solution:
    @staticmethod
    def fib(n: int) -> int:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 0338-Counting-Bits.py"""
        # Initialize a list to store the Fibonacci numbers with length n + 1
        fibonacci = [0, 1] + [0] * (n - 1)
        # To get to the F(n) Fibonacci number, loop n - 1 times from 2 to n
        for i in range(2, n + 1):
            # Calculate the current Fibonacci number by adding the two preceding ones
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
        # Return the F(n) Fibonacci number
        return fibonacci[n]

    @staticmethod
    def fibOptimal(n: int) -> int:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0070-Climbing-Stairs.py"""
        # Base case for "one": if n = 0, return 0
        if n == 0:
            return 0
        # Initialize two variables to store the two preceding Fibonacci numbers
        one, two = 0, 1
        # To get to the F(n) Fibonacci number, loop n - 1 times because we already have F(0) and F(1)
        for _ in range(n - 1):
            # Calculate the current Fibonacci number "two" by adding the two preceding numbers
            # Update "one" too for the next iteration's calculation
            one, two = two, one + two
        # Return the F(n) Fibonacci number
        return two


# Input = 2, Output = 1
assert Solution.fib(2) == 1

# Input = 3, Output = 2
assert Solution.fib(3) == 2

# Input = 4, Output = 3
assert Solution.fibOptimal(4) == 3

print("All unit tests are passed.")

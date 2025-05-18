"""1137. N-th Tribonacci Number
Link: https://leetcode.com/problems/n-th-tribonacci-number/
Difficulty: Easy
Description: The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn = Tn-1 + Tn-2 + Tn-3 for n > 2.
Given n, return the value of Tn."""


class Solution:
    @staticmethod
    def tribonacci(n: int) -> int:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0509-Fibonacci-Number.py"""
        # Base case: n = 0, 1, 2
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Initialize the Tribonacci sequence
        t0, t1, t2 = 0, 1, 1

        # Calculate the Tribonacci number for n
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2


# Input = 4, Output = 4
assert Solution.tribonacci(4) == 4

# Input = 25, Output = 1389537
assert Solution.tribonacci(25) == 1389537

# Input = 37, Output = 2082876103
assert Solution.tribonacci(37) == 2082876103

print("All unit tests are passed.")

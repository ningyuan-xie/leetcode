"""2894. Divisible and Non-divisible Sums Difference
Link: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
Difficulty: Easy
Description: You are given positive integers n and m.
Define two integers as follows:
- num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
- num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2."""


class Solution:
    @staticmethod
    def differenceOfSums(n: int, m: int) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        num1, num2 = 0, 0

        for i in range(1, n+1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i

        return num1 - num2


# Unit Test: n = 10, m = 3, Output: 19
assert Solution.differenceOfSums(10, 3) == 19

# Unit Test: n = 5, m = 6, Output: 15
assert Solution.differenceOfSums(5, 6) == 15

# Unit Test: n = 5, m = 1, Output: -15
assert Solution.differenceOfSums(5, 1) == -15

print("All unit tests are passed.")

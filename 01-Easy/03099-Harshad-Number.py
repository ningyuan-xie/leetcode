"""3099. Harshad Number
Link: https://leetcode.com/problems/harshad-number/
Difficulty: Easy
Description: An integer divisible by the sum of its digits is said to be a Harshad number.
You are given an integer x. Return the sum of the digits of x if x is a Harshad number,
otherwise, return -1."""


class Solution:
    @staticmethod
    def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(log(x)), Space Complexity: O(1)"""
        sum_of_digits = sum(int(digit) for digit in str(x))

        return sum_of_digits if x % sum_of_digits == 0 else -1


# Unit Test: x = 18, Output = 9
assert Solution.sumOfTheDigitsOfHarshadNumber(18) == 9

# Unit Test: x = 23, Output = -1
assert Solution.sumOfTheDigitsOfHarshadNumber(23) == -1

print("All unit tests are passed.")

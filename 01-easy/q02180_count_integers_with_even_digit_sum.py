"""2180. Count Integers With Even Digit Sum
Link: https://leetcode.com/problems/count-integers-with-even-digit-sum/
Difficulty: Easy
Description: Given a positive integer num, return the number of positive integers less than or equal
to num whose digit sums are even.
The digit sum of a positive integer is the sum of all its digits."""


class Solution:
    @staticmethod
    def countEven(num: int) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n), Space Complexity: O(1)."""

        def digitSum(n: int) -> int:
            """Helper Function: Calculate the sum of digits of a number"""
            return sum(int(digit) for digit in str(n))

        count = 0
        for i in range(1, num + 1):
            if digitSum(i) % 2 == 0:
                count += 1
        return count


# Unit Test: num = 4, Output: 2
assert Solution.countEven(4) == 2

# Unit Test: num = 30, Output: 14
assert Solution.countEven(30) == 14

print("All unit tests are passed.")

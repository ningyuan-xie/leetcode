"""2520. Count the Digits That Divide a Number
Link: https://leetcode.com/problems/count-the-digits-that-divide-a-number/
Difficulty: Easy
Description: You are given an integer number. You need to count the number of digits that divide the number.
- A digit d divides a number if the number is divisible by d."""

from typing import List


class Solution:
    @staticmethod
    def countDividingDigits(num: int) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n * m), Space Complexity: O(1)"""
        # Initialize the answer to 0
        ans = 0
        # Iterate through each digit of the number
        for digit in str(num):
            # Check if the digit divides the number
            if int(digit) != 0 and num % int(digit) == 0:
                # Increment the answer if the digit divides the number
                ans += 1
        return ans


# Unit Test: n = 7, Output: 1
assert Solution.countDividingDigits(7) == 1

# Unit Test: n = 121, Output: 2
assert Solution.countDividingDigits(121) == 2

# Unit Test: n = 1248, Output: 4
assert Solution.countDividingDigits(1248) == 4

print("All unit tests are passed")

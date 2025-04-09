"""2160. Minimum Sum of Four-Digit Number After Splitting Digits
Link: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
Difficulty: Easy
Description: You are given a positive integer num consisting of exactly four digits. Split num into
two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1
and new2, and all the digits found in num must be used.
- For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of
the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2."""

from typing import List


class Solution:
    @staticmethod
    def minimumSum(num: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)"""
        # Convert num to a list of digits
        digits = [int(digit) for digit in str(num)]
        digits.sort()  # 2932 -> [2, 3, 9, 2] -> [2, 2, 3, 9]

        # Calculate new1 and new2
        new1, new2 = 0, 0
        for (i, digit) in enumerate(digits):
            # Alternate digits to new1 and new2
            if i % 2 == 0:
                new1 = new1 * 10 + digit
            else:
                new2 = new2 * 10 + digit

        return new1 + new2


# Unit Test: num = 2932, Output: 52
assert Solution.minimumSum(2932) == 52

# Unit Test: num = 4009, Output: 13
assert Solution.minimumSum(4009) == 13

print("All unit tests are passed.")

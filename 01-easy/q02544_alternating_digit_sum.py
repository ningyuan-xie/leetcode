"""2544. Alternating Digit Sum
Link: https://leetcode.com/problems/alternating-digit-sum/
Difficulty: Easy
Description: You are given a positive integer n. Each digit of n has a sign according to the
following rules:
- The most significant digit is assigned a positive sign.
- Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign."""


class Solution:
    @staticmethod
    def alternatingDigitSum(n: int) -> int:
        """Optimal Solution: Int and String Conversion. Time Complexity: O(n), Space Complexity: O(1)."""
        alternating_sum = 0

        for i, digit in enumerate(str(n)):
            alternating_sum += int(digit) if i % 2 == 0 else -int(digit)

        return alternating_sum


# Input: n = 521, Output: 4
assert Solution.alternatingDigitSum(521) == 4

# Input: n = 111, Output: 1
assert Solution.alternatingDigitSum(111) == 1

# Input: n = 886996, Output: 0
assert Solution.alternatingDigitSum(886996) == 0

print("All unit tests are passed.")

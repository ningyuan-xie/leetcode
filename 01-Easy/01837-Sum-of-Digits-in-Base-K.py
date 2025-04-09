"""1837. Sum of Digits in Base K
Link: https://leetcode.com/problems/sum-of-digits-in-base-k/
Difficulty: Easy
Description: Given an integer n (in base 10) and a base k, return the sum of the digits of n after
converting n from base 10 to base k.
After converting, each digit should be interpreted as a base 10 number, and the sum should be
returned in base 10."""


class Solution:
    @staticmethod
    def sumBase(n: int, k: int) -> int:
        """Optimal Solution: Base Conversion. Time Complexity: O(log(n)), Space Complexity: O(1)"""
        # Initialize the sum of digits in base k
        digit_sum = 0

        # Perform base conversion and calculate the sum of digits
        while n > 0:
            digit_sum += n % k  # Extract the last digit in base k: 34 % 6 = 4; 5 % 6 = 5
            n //= k  # Reduce n by removing the last digit in base k: 34 // 6 = 5; 5 // 6 = 0

        # Return the total sum of the digits
        return digit_sum


# Unit Test: n = 34, k = 6, Output: 9
# 34 in base 6 is 5 * 6^1 + 4 * 6^0 = 30 + 4 = 34
assert Solution.sumBase(34, 6) == 9

# Unit Test: n = 10, k = 10, Output: 1
# 10 in base 10 is 1 * 10^1 + 0 * 10^0 = 10 + 0 = 10
assert Solution.sumBase(10, 10) == 1

# Unit Test: n = 42, k = 2, Output: 3
# 42 in base 2 is 1 * 2^5 + 0 * 2^4 + 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 32 + 8 + 2 = 42
assert Solution.sumBase(42, 2) == 3

# Unit Test: n = 8, k = 2, Output: 1
# 8 in base 2 is 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 0 * 2^0 = 8
assert Solution.sumBase(8, 2) == 1

print("All unit tests are passed.")

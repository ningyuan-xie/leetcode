"""3536. Maximum Product of Two Digits
Link: https://leetcode.com/problems/maximum-product-of-two-digits/
Difficulty: Easy
Description: You are given a positive integer n.
Return the maximum product of any two digits in n.
Note: You may use the same digit twice if it appears more than once in n."""


class Solution:
    @staticmethod
    def maxProduct(n: int) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        max1 = max2 = 0

        # Update max1 and max2
        for digit in str(n):
            digit = int(digit)
            if digit > max1:
                max1, max2 = digit, max1
            elif digit > max2:
                max2 = digit
        
        return max1 * max2


def unit_tests():
    # Input: n = 31, Output: 3
    assert Solution.maxProduct(31) == 3

    # Input: n = 22, Output: 4
    assert Solution.maxProduct(22) == 4

    # Input: n = 124, Output: 8
    assert Solution.maxProduct(124) == 8


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

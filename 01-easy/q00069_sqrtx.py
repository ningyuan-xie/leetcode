"""69. Sqrt(x)
Link: https://leetcode.com/problems/sqrtx/
Difficulty: Easy
Description: Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
• For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""


class Solution:
    @staticmethod
    def mySqrt(x: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        # When the loop ends, right is the largest integer such that right * right <= x
        return right

def unit_tests():
    # Input: x = 4, Output: 2
    assert Solution.mySqrt(4) == 2

    # Input: x = 8, Output: 2
    assert Solution.mySqrt(8) == 2

    # Input: x = 1, Output: 1
    assert Solution.mySqrt(1) == 1

    # Input: x = 0, Output: 0
    assert Solution.mySqrt(0) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

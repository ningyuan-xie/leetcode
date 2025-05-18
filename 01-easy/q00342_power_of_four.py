"""342. Power of Four
Link: https://leetcode.com/problems/power-of-four/
Difficulty: Easy
Description: Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x."""


class Solution:
    @staticmethod
    def isPowerOfFour(n: int) -> bool:
        """Optimal Solution: Recursion. Time Complexity: O(log(n)), Space Complexity: O(log(n))."""
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # Base case: if n is equal to 1, return True
        if n == 1:
            return True
        # If n is divisible by 4, then recursively check if n // 4 is a power of 4
        return n % 4 == 0 and Solution.isPowerOfFour(n // 4)


def unit_tests():
    # Input: n = 16, Output: True
    assert Solution.isPowerOfFour(16) is True

    # Input: n = 5, Output: False
    assert Solution.isPowerOfFour(5) is False

    # Input: n = 1, Output: True
    assert Solution.isPowerOfFour(1) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

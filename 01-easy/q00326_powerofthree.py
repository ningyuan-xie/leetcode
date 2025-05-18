"""326. Power of Three
Link: https://leetcode.com/problems/power-of-three/
Difficulty: Easy
Description: Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x."""


class Solution:
    @staticmethod
    def isPowerOfThree(n: int) -> bool:
        """Optimal Solution: Recursion. Time Complexity: O(log(n)), Space Complexity: O(log(n)).
        Similar to 231. Power of Two."""
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # Base case: if n is equal to 1, return True
        if n == 1:
            return True
        # If n is divisible by 3, then recursively check if n // 3 is a power of 3
        return n % 3 == 0 and Solution.isPowerOfThree(n // 3)


def unit_tests():
    # Input: n = 27, Output: True
    assert Solution.isPowerOfThree(27) is True

    # Input: n = 0, Output: False
    assert Solution.isPowerOfThree(0) is False

    # Input: n = 9, Output: True
    assert Solution.isPowerOfThree(9) is True

    # Input: n = 45, Output: False
    assert Solution.isPowerOfThree(45) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

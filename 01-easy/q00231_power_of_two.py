"""231. Power of Two
Link: https://leetcode.com/problems/power-of-two/
Difficulty: Easy
Description: Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x."""


class Solution:
    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        """Optimal Solution: Recursion. Time Complexity: O(log(n)), Space Complexity: O(log(n))."""
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # Base case: if n is 1, return True (2^0 = 1)
        if n == 1:
            return True
        # Recursive case: check if n is divisible by 2 and call the function recursively with n divided by 2
        return n % 2 == 0 and Solution.isPowerOfTwo(n // 2)


def unit_tests():
    # Input: 1, Output: true
    assert Solution.isPowerOfTwo(1) is True

    # Input: 16, Output: true
    assert Solution.isPowerOfTwo(16) is True

    # Input: 3, Output: false
    assert Solution.isPowerOfTwo(3) is False

    # Input: 4, Output: true
    assert Solution.isPowerOfTwo(4) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

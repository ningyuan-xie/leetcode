"""263. Ugly Number
Link: https://leetcode.com/problems/ugly-number/
Difficulty: Easy
Description: An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
Given an integer n, return true if n is an ugly number."""


class Solution:
    @staticmethod
    def isUgly(n: int) -> bool:
        """Optimal Solution: While Loop. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        # Check if n is less than or equal to 0
        if n <= 0:
            return False
        
        # Continuously divide n by 2, 3, and 5 until undivisible by any of them
        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i
        
        # If n is reduced to 1, it is an ugly number
        return n == 1


def unit_tests():
    # Input: num = 6, Output: True
    assert Solution.isUgly(6) is True

    # Input: num = 8, Output: True
    assert Solution.isUgly(8) is True

    # Input: num = 14, Output: False
    assert Solution.isUgly(14) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

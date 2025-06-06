"""693. Binary Number with Alternating Bits
Link: https://leetcode.com/problems/binary-number-with-alternating-bits/
Difficulty: Easy
Description: Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values."""


class Solution:
    @staticmethod
    def hasAlternatingBits(n: int) -> bool:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1)."""
        # If n has alternating bits like 101, n >> 1 = 10, x = 101 ^ 10 = 111
        # If n has non-alternating bits like 111, n >> 1 = 11, x = 111 ^ 11 = 100
        x = n ^ (n >> 1)

        # If x is a sequence of 1s like 111, x + 1 = 1000, x & (x + 1) = 111 & 1000 = 0
        return (x & (x + 1)) == 0


def unit_tests():
    # Input: n = 5, Output: True
    assert Solution.hasAlternatingBits(5) is True

    # Input: n = 7, Output: False
    assert Solution.hasAlternatingBits(7) is False

    # Input: n = 11, Output: False
    assert Solution.hasAlternatingBits(11) is False

    # Input: n = 10, Output: True
    assert Solution.hasAlternatingBits(10) is True

    # Input: n = 4, Output: False
    assert Solution.hasAlternatingBits(4) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""1009. Complement of Base 10 Integer
Link: https://leetcode.com/problems/complement-of-base-10-integer/
Difficulty: Easy
Description: The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
• For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement."""


class Solution:
    @staticmethod
    def bitwiseComplement(n: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1).
        Same as 476. Number-Complement."""
        # Initialize mask to 1
        mask = 1

        # Create a mask with all bits set to 1 for the length of n
        while mask < n:
            mask = (mask << 1) | 1

        # XOR n with the mask to get the complement
        return n ^ mask


def unit_tests():
    # Input: n = 5 (101), Output: 2 (010)
    assert Solution.bitwiseComplement(5) == 2

    # Input: n = 1, Output: 0
    assert Solution.bitwiseComplement(1) == 0

    # Input: n = 7, Output: 0
    assert Solution.bitwiseComplement(7) == 0

    # Input: n = 10, Output: 5
    assert Solution.bitwiseComplement(10) == 5

    # Input: n = 0, Output: 1
    assert Solution.bitwiseComplement(0) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

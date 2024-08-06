"""1009. Complement of Base 10 Integer
Link: https://leetcode.com/problems/complement-of-base-10-integer/
Difficulty: Easy
Description: The complement of an integer is the integer you get when you
flip all the 0's to 1's and all the 1's to 0's in its binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement."""


class Solution:
    @staticmethod
    def bitwiseComplement(n: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1).
           Bitwise XOR operator ^ : 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0.
           Similar to 0476-Number-Complement.py"""
        # Base case: If the number is 0, return 1
        if n == 0:
            return 1

        # Find the number of bits in the number
        num_bits = n.bit_length()  # E.g. n = 5 (101) -> num_bits = 3

        # Construct a mask with all bits set to 1, which can be used to flip all the bits
        # Shift 1 to the left by the number of bits and subtract 1
        mask = (1 << num_bits) - 1  # 1000 -1 = 111

        # XOR the number with the mask to flip all the bits: 5 (101) ^ 7 (111) = 2 (010)
        return n ^ mask


# Unit Test: Input: n = 5 (101), Output: 2 (010)
assert Solution.bitwiseComplement(5) == 2

# Unit Test: Input: n = 1, Output: 0
assert Solution.bitwiseComplement(1) == 0

# Unit Test: Input: n = 7, Output: 0
assert Solution.bitwiseComplement(7) == 0

# Unit Test: Input: n = 10, Output: 5
assert Solution.bitwiseComplement(10) == 5

# Unit Test: Input: n = 0, Output: 1
assert Solution.bitwiseComplement(0) == 1

print("All unit tests are passed")

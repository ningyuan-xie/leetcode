"""476. Number Complement
Link: https://leetcode.com/problems/number-complement/
Difficulty: Easy
Description: Given a positive integer num, output its complement number.
The complement strategy is to flip the bits of its binary representation."""


class Solution:
    @staticmethod
    def findComplement(num: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1).
           Bitwise XOR operator ^ : 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0.
           Similar to 0190-Reverse-Bits.py"""
        # Find the number of bits in the number
        num_bits = num.bit_length()  # E.g. num = 5 (101) -> num_bits = 3

        # Construct a mask with all bits set to 1, which can be used to flip all the bits
        # Shift 1 to the left by the number of bits and subtract 1
        mask = (1 << num_bits) - 1  # 1000 -1 = 111

        # XOR the number with the mask to flip all the bits: 5 (101) ^ 7 (111) = 2 (010)
        return num ^ mask


# Input: num = 5 (101), Output: 2 (010)
assert Solution.findComplement(5) == 2

# Input: num = 1, Output: 0
assert Solution.findComplement(1) == 0

# Input: num = 7, Output: 0
assert Solution.findComplement(7) == 0

# Input: num = 10, Output: 5
assert Solution.findComplement(10) == 5

print("All unit tests are passed.")

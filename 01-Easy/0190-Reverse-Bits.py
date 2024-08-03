"""190. Reverse Bits
Link: https://leetcode.com/problems/reverse-bits/
Difficulty: Easy
Description: Reverse bits of a given 32 bits unsigned integer."""


class Solution:
    @staticmethod
    def reverseBits(n: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1).
           Similar to the reverse method in 02-Medium/0007-Reverse-Integer.py"""
        # Initialize result in binary
        result = 0  # 00000000000000000000000000000000
        # Traverse the 32 bits of the given integer from RIGHT to LEFT
        for i in range(32):
            # Shift the result to the left by 1 bit, leaving room for the next bit to be added
            result <<= 1  # 001 -> 010 -> 100
            # n & 1 extracts the rightmost bit of n, as 1 in binary only has its rightmost bit = 1
            # result |= n & 1 adds this rightmost bit of the given integer to the result
            result |= n & 1  # |= is the bitwise OR assignment operator, similar to += for addition
            # n is shifted to the right by 1 bit, removing the bit just added to result
            n >>= 1  # 100 -> 010 -> 001 -> 000

        # E.g. 5 (00000000000000000000000000000101) -> 2684354560 (10100000000000000000000000000000)
        return result


# Unit Test:
# 43261596 (00000010100101000001111010011100) -> 964176192 (00111001011110000010100101000000)
assert Solution.reverseBits(43261596) == 964176192

# Unit Test:
# 4294967293 (00000011111111111111111111111101) -> 3221225471 (10111111111111111111111111111111)
assert Solution.reverseBits(4294967293) == 3221225471

print("All unit tests are passed")

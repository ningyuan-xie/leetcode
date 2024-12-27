"""2220. Minimum Bit Flips to Convert Number
Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
Difficulty: Easy
Description: A bit flip of a number x is choosing a bit in the binary representation of x and
flipping it from either 0 to 1 or 1 to 0.
- For example, for x = 7, the binary representation is 111 and we may choose any bit (including
any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110,
flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero)
to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal."""


class Solution:
    @staticmethod
    def minBitFlips(start: int, goal: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1).
           Bitwise XOR operator ^ : 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0.
           Bitwise AND operator & : 1 & 1 = 1, 1 & 0 = 0, 0 & 0 = 0.
           Same as 0461-Hamming-Distance.py"""
        # Initialize the Hamming distance
        hamming_distance = 0
        # Calculate the XOR of x and y
        xor = start ^ goal  # E.g. start = 1 (0001), goal = 4 (0100) -> xor = 5 (0101)
        # Count the number of set bits in the XOR from RIGHT to LEFT
        while xor:
            hamming_distance += xor & 1  # Add the rightmost bit of the XOR to the Hamming distance
            xor >>= 1  # Shift the xor to the right by 1, removing the bit just added
        return hamming_distance


# Unit Test: start = 10, goal = 7, Output: 3
assert Solution.minBitFlips(10, 7) == 3

# Unit Test: start = 3, goal = 4, Output: 3
assert Solution.minBitFlips(3, 4) == 3

print("All unit tests are passed")

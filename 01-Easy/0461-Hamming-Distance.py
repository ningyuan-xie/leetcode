# Link: https://leetcode.com/problems/hamming-distance/
# Difficulty: Easy
# Description: The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.

class Solution:
    # Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1)
    # Similar to 0190-Reverse-Bits.py and 0191-Number-of-1-Bits.py
    @staticmethod
    def hammingDistance(x: int, y: int) -> int:
        # Initialize the Hamming distance
        hamming_distance = 0
        # Calculate the XOR of x and y
        xor = x ^ y  # E.g. x = 1 (0001), y = 4 (0100) -> xor = 5 (0101)
        # Count the number of set bits in the XOR from RIGHT to LEFT
        while xor:
            hamming_distance += xor & 1  # Add the rightmost bit of the XOR to the Hamming distance
            xor >>= 1  # Shift the xor to the right by 1, removing the bit just added
        return hamming_distance


# Unit Test: Input: x = 1, y = 4, Output: 2
assert Solution.hammingDistance(1, 4) == 2

# Unit Test: Input: x = 3, y = 1, Output: 1
assert Solution.hammingDistance(3, 1) == 1

# Unit Test: Input: x = 0, y = 0, Output: 0
assert Solution.hammingDistance(0, 0) == 0

print("All unit tests are passed")

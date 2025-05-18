"""190. Reverse Bits
Link: https://leetcode.com/problems/reverse-bits/
Difficulty: Easy
Description: Reverse bits of a given 32 bits unsigned integer."""


class Solution:
    @staticmethod
    def reverseBits(n: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1).
        0 & 0 = 0, 0 & 1 = 0, 1 & 1 = 1. 0 | 0 = 0, 0 | 1 = 1, 1 | 1 = 1."""
        result = 0
        
        # Traverse the 32 bits of the given integer from RIGHT to LEFT
        for i in range(32):
            # Shift the result to the left by 1 bit to make space for the next bit
            result <<= 1
            # Add the rightmost bit of n to the result using & and |
            result |= n & 1
            # Shift n to the right by 1 bit, removing the rightmost bit
            n >>= 1
        return result


def unit_tests():
    # Input: n = 43261596, Output: 964176192
    assert Solution.reverseBits(43261596) == 964176192

    # Input: n = 4294967293, Output: 3221225471
    assert Solution.reverseBits(4294967293) == 3221225471


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

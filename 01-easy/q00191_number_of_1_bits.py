"""191. Number of 1 Bits
Link: https://leetcode.com/problems/number-of-1-bits/
Difficulty: Easy
Description: Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight)."""


class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1)."""
        count = 0
        
        # Traverse the 32 bits of the given integer from RIGHT to LEFT
        for i in range(32):
            # Increment count if the rightmost bit is 1
            count += n & 1
            # Shift n to the right by 1 bit, removing the rightmost bit
            n >>= 1
        return count


def unit_tests():
    # Input: n = 11, Output: 3
    assert Solution.hammingWeight(11) == 3

    # Input: n = 128, Output: 1
    assert Solution.hammingWeight(128) == 1

    # Input: n = 2147483647, Output: 31
    assert Solution.hammingWeight(2147483647) == 31


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

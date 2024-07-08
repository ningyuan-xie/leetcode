# Link: https://leetcode.com/problems/number-of-1-bits/
# Difficulty: Easy
# Description: Write a function that takes an unsigned integer
# and returns the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    # Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1)
    @staticmethod
    def hammingWeight(n: int) -> int:
        # Initialize the number of '1' bits
        count = 0
        # Traverse the 32 bits of the given integer from right to left
        for i in range(32):
            # Check if the rightmost bit of n is 1
            # If it is, increment the count of '1' bits
            count += n & 1
            # Shift n to the right by 1 bit, removing the rightmost bit
            n >>= 1
        return count


# Unit Test: Input: n = 11 (00000000000000000000000000001011), Output: 3
assert Solution.hammingWeight(11) == 3

# Unit Test: Input: n = 128 (00000000000000000000000010000000), Output: 1
assert Solution.hammingWeight(128) == 1

# Unit Test: Input: n = 2147483647 (01111111111111111111111111111111), Output: 31
assert Solution.hammingWeight(2147483647) == 31

print("All unit tests are passed")

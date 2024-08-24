"""868. Binary Gap
Link: https://leetcode.com/problems/binary-gap/
Difficulty: Easy
Description: Given a positive integer n, find and return the longest distance between any two
adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0."""


class Solution:
    @staticmethod
    def binaryGap(n: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(log(n)), Space Complexity: O(1)
           Bitwise AND operator & : 1 & 1 = 1, 1 & 0 = 0, 0 & 0 = 0."""
        # Initialize the longest distance between two adjacent 1's
        longest_distance = 0
        # Initialize the previous position of 1 as -1
        prev_position = -1

        # Iterate through the bits of n
        for i in range(32):
            # If the i-th bit is 1
            if (n >> i) & 1:  # n >> i shifts the bits of n to the right by i positions: 101 >> 1 = 10
                # If the previous position is not -1, update the longest distance
                if prev_position != -1:
                    longest_distance = max(longest_distance, i - prev_position)
                # Update the previous position
                prev_position = i

        return longest_distance


# Unit Test: Input: 22, Output: 2. Explanation: 22 in binary is 10110, so the longest distance is 2
assert Solution.binaryGap(22) == 2

# Unit Test: Input: 5, Output: 2. Explanation: 5 in binary is 101, so the longest distance is 2
assert Solution.binaryGap(5) == 2

# Unit Test: Input: 6, Output: 1. Explanation: 6 in binary is 110, so the longest distance is 1
assert Solution.binaryGap(6) == 1

# Unit Test: Input: 8, Output: 0. Explanation: 8 in binary is 1000, so there are no two adjacent 1's
assert Solution.binaryGap(8) == 0

print("All unit tests are passed")

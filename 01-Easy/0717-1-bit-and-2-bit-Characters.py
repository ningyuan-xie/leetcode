"""717. 1-bit and 2-bit Characters
Link: https://leetcode.com/problems/1-bit-and-2-bit-characters/
Difficulty: Easy
Description: We have two special characters: The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11). Given a binary array bits
that ends with 0, return true if the last character must be a one-bit character."""

from typing import List


class Solution:
    @staticmethod
    def is_one_bit_character(bits: List[int]) -> bool:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1).
           The solution uses a greedy approach, making local decisions at each step to skip ahead
           in the list based on the current bit value"""
        # Initialize the index to traverse the list of bits
        i = 0

        # Greedy approach: once a decision is made to move one or two steps forward, the algorithm
        # never revisits previous bits or re-evaluates past decisions (no backtracking)
        while i < len(bits) - 1:
            # If the current bit is 0, it is a one-bit character: move one bit to the right
            if bits[i] == 0:
                i += 1
            # If the current bit is 1, it is a two-bit character: move two bits to the right
            else:
                i += 2

        # If the index is at the last bit, the last char is a standalone one-bit character
        return i == len(bits) - 1


# Unit Test: Input: bits = [1, 0, 0], Output: True
assert Solution.is_one_bit_character([1, 0, 0]) is True

# Unit Test: Input: bits = [1, 1, 1, 0], Output: False
assert Solution.is_one_bit_character([1, 1, 1, 0]) is False

# Unit Test: Input: bits = [0], Output: True
assert Solution.is_one_bit_character([0]) is True

print("All unit tests are passed")

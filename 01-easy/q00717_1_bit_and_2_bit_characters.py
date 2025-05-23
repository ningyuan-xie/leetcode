"""717. 1-bit and 2-bit Characters
Link: https://leetcode.com/problems/1-bit-and-2-bit-characters/
Difficulty: Easy
Description: We have two special characters:
• The first character can be represented by one bit 0.
• The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character."""

from typing import List


class Solution:
    @staticmethod
    def is_one_bit_character(bits: List[int]) -> bool:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(bits)
        i = 0
        
        while i < n - 1:
            # 1-bit character if 0, 2-bit character if 1 (since 1 must be followed by 0 or 1)
            i += 1 if bits[i] == 0 else 2
            
        # Check if we ended exactly at the last character (which must be 0)
        return i == n - 1


def unit_tests():
    # Input: bits = [1, 0, 0], Output: True
    assert Solution.is_one_bit_character([1, 0, 0]) is True

    # Input: bits = [1, 1, 1, 0], Output: False
    assert Solution.is_one_bit_character([1, 1, 1, 0]) is False

    # Input: bits = [0], Output: True
    assert Solution.is_one_bit_character([0]) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

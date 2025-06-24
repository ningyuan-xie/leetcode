"""2729. Check if The Number is Fascinating
Link: https://leetcode.com/problems/check-if-the-number-is-fascinating/
Difficulty: Easy
Description: You are given an integer n that consists of exactly 3 digits.
We call the number n fascinating if, after the following modification, the resulting number contains
all the digits from 1 to 9 exactly once and does not contain any 0's:
- Concatenate n with the numbers 2 * n and 3 * n.
Return true if n is fascinating, or false otherwise.
Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371
is 121371."""

from typing import List


class Solution:
    @staticmethod
    def isFascinating(n: int) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(1), Space Complexity: O(1)."""
        # Concatenate the numbers
        concatenated = str(n) + str(2 * n) + str(3 * n)

        # Check if the concatenated number has exactly 9 digits
        if len(concatenated) != 9:
            return False

        # Check if the concatenated number contains all the digits from 1 to 9 exactly once
        freq = {}
        for digit in concatenated:
            if digit == "0":
                return False
            freq[digit] = freq.get(digit, 0) + 1
        return len(freq) == 9


# Input: n = 192, Output: True
assert Solution.isFascinating(192) is True

# Input: n = 100, Output: False
assert Solution.isFascinating(100) is False

# Input: n = 783, Output: False
assert Solution.isFascinating(783) is False

print("All unit tests are passed.")

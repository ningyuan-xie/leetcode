"""1758. Minimum Changes To Make Alternating Binary String
Link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
Difficulty: Easy
Description: You are given a string s consisting only of the characters '0' and '1'. In one
operation, you can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the
string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating."""

from typing import List


class Solution:
    @staticmethod
    def min_operations(s: str) -> int:
        """Optimal Solution: One Pass. Time Complexity: O(n), Space Complexity: O(1)"""
        pattern0_operations = 0  # Mismatches for "010101..."
        pattern1_operations = 0  # Mismatches for "101010..."

        for i in range(len(s)):
            # Expected character if the pattern starts with '0'
            expected_char0 = '0' if i % 2 == 0 else '1'
            # Expected character if the pattern starts with '1'
            expected_char1 = '1' if i % 2 == 0 else '0'

            # Count mismatches for each pattern
            if s[i] != expected_char0:
                pattern0_operations += 1
            if s[i] != expected_char1:
                pattern1_operations += 1

        # Return the minimum of the two patterns' mismatch counts
        return min(pattern0_operations, pattern1_operations)


# Unit Test: s = "0100", Output: 1
assert Solution.min_operations("0100") == 1

# Unit Test: s = "10", Output: 0
assert Solution.min_operations("10") == 0

# Unit Test: s = "1111", Output: 2
assert Solution.min_operations("1111") == 2

print("All unit tests are passed.")

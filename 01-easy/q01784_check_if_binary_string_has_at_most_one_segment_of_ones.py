"""1784. Check if Binary String Has at Most One Segment of Ones
Link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
Difficulty: Easy
Description: Given a binary string s without leading zeros, return true if s contains at most one
contiguous segment of ones. Otherwise, return false."""


class Solution:
    @staticmethod
    def check_ones_segment(s: str) -> bool:
        """Optimal Solution: Check Pattern. Time Complexity: O(n), Space Complexity: O(1).
           To determine if there's only one contiguous segment of '1's, we can check for occurrences
           of the pattern "01" in the string. If "01" appears, it means there's a transition from
           '1's to '0's, followed by another '1' later, indicating more than one segment of '1's"""
        return "01" not in s


# Input: s = "1001", Output: False
assert Solution.check_ones_segment("1001") is False

# Input: s = "110", Output: True
assert Solution.check_ones_segment("110") is True

# Input: s = "1", Output: True
assert Solution.check_ones_segment("1") is True

print("All unit tests are passed.")

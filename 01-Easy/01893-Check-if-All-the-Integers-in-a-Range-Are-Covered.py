"""1893. Check if All the Integers in a Range Are Covered
Link: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
Difficulty: Easy
Description: You are given a 2D integer array ranges and two integers left and right. Each
ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.
Return true if each integer in the inclusive range [left, right] is covered by at least one interval
in ranges. Return false otherwise.
An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi."""

from typing import List


class Solution:
    @staticmethod
    def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
        """Optimal Solution: Brute Force. Time Complexity: O(n * m), Space Complexity: O(1)"""
        # Initialize covered to False
        for x in range(left, right + 1):
            covered = False

            # Check if the integer is covered by at least one interval
            for (left_i, right_i) in ranges:
                if left_i <= x <= right_i:
                    covered = True
                    break  # Skip the rest of the intervals and move to the next integer

            # The integer is not covered by any interval
            if not covered:
                return False
        return True


# Unit Test: ranges = [[1, 2], [3, 4], [5, 6]], left = 2, right = 5, Output: True
assert Solution.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5) is True

# Unit Test: ranges = [[1, 10], [10, 20]], left = 21, right = 21, Output: False
assert Solution.isCovered([[1, 10], [10, 20]], 21, 21) is False

print("All unit tests are passed.")

"""1051. Height Checker
Link: https://leetcode.com/problems/height-checker/
Difficulty: Easy
Description: A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i]."""

from typing import List


class Solution:
    @staticmethod
    def heightChecker(heights: List[int]) -> int:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(n)."""
        # Create sorted array to compare against
        expected = sorted(heights)
        
        # Count positions where heights differ from expected
        mismatch_count = sum(1 for i in range(len(heights)) if heights[i] != expected[i])
        
        return mismatch_count


def unit_tests():
    # Input: heights = [1, 1, 4, 2, 1, 3], Output: 3
    assert Solution.heightChecker([1, 1, 4, 2, 1, 3]) == 3

    # Input: heights = [5, 1, 2, 3, 4], Output: 5
    assert Solution.heightChecker([5, 1, 2, 3, 4]) == 5

    # Input: heights = [1, 2, 3, 4, 5], Output: 0
    assert Solution.heightChecker([1, 2, 3, 4, 5]) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

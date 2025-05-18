"""561. Array Partition I
Link: https://leetcode.com/problems/array-partition/
Difficulty: Easy
Description: Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum."""

from typing import List


class Solution:
    @staticmethod
    def arrayPairSum(nums: List[int]) -> int:
        """Optimal Solution: Sort. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        nums.sort()

        # Sum the elements at even indices
        return sum(nums[::2])


def unit_tests():
    # Input: nums = [1, 4, 3, 2], Output: 4
    assert Solution.arrayPairSum([1, 4, 3, 2]) == 4

    # Input: nums = [6, 2, 6, 5, 1, 2], Output: 9
    assert Solution.arrayPairSum([6, 2, 6, 5, 1, 2]) == 9


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

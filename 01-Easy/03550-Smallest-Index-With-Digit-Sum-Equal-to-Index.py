"""3550. Smallest Index With Digit Sum Equal to Index
Link: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
Difficulty: Easy
Description: You are given an integer array nums.
Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
If no such index exists, return -1."""

from typing import List


class Solution:
    @staticmethod
    def smallestIndex(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        for i in range(len(nums)):
            if sum(int(digit) for digit in str(nums[i])) == i:
                return i
        return -1


def unit_tests():
    # Input: nums = [1,3,2], Output: 2
    assert Solution.smallestIndex([1,3,2]) == 2

    # Input: nums = [1,10,11], Output: 1
    assert Solution.smallestIndex([1,10,11]) == 1

    # Input: nums = [1,2,3], Output: -1
    assert Solution.smallestIndex([1,2,3]) == -1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

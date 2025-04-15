"""3423. Maximum Difference Between Adjacent Elements in a Circular Array
Link: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
Difficulty: Easy
Description: Given a circular array nums, find the maximum absolute difference between adjacent elements.
Note: In a circular array, the first and last elements are adjacent."""

from typing import List


class Solution:
    @staticmethod
    def maxAdjacentDifference(nums: List[int]) -> int:
        """Optimal Solution: Circular Array. Time Complexity: O(n), Space Complexity: O(1)"""
        n = len(nums)
        max_diff = 0

        for i in range(n):
            # Calculate the absolute difference between adjacent elements
            diff = abs(nums[i] - nums[(i + 1) % n])
            max_diff = max(max_diff, diff)

        return max_diff


def unit_tests():
    # Input: nums = [1,2,4], Output: 3
    assert Solution.maxAdjacentDifference([1, 2, 4]) == 3

    # Input: nums = [-5,-10,-5], Output: 5
    assert Solution.maxAdjacentDifference([-5, -10, -5]) == 5


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

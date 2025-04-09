"""2016. Maximum Difference Between Increasing Elements
Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
Difficulty: Easy
Description: Given a 0-indexed integer array nums of size n, find the maximum difference between
nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
Return the maximum difference. If no such i and j exists, return -1."""

from typing import List


class Solution:
    @staticmethod
    def maximumDifference(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0121-Best-Time-to-Buy-and-Sell-Stock.py"""
        # Initialize the maximum difference
        max_diff = -1
        # Initialize the minimum number encountered so far
        min_num = nums[0]

        for i in range(1, len(nums)):
            # Update the maximum difference
            max_diff = max(max_diff, nums[i] - min_num)
            # Update the minimum number encountered so far
            min_num = min(min_num, nums[i])

        return max_diff


# Unit Test: nums = [7, 1, 5, 4], Output: 4
assert Solution.maximumDifference([7, 1, 5, 4]) == 4

# Unit Test: nums = [9, 4, 3, 2], Output: -1
assert Solution.maximumDifference([9, 4, 3, 2]) == -1

# Unit Test: nums = [1, 5, 2, 10], Output: 9
assert Solution.maximumDifference([1, 5, 2, 10]) == 9

print("All unit tests are passed.")

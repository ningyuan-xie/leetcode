"""1984. Minimum Difference Between Highest and Lowest of K Scores
Link: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores
Difficulty: Easy
Description: You are given a 0-indexed integer array nums, where nums[i] represents the score of
the ith student. You are also given an integer k.
Pick the scores of any k students from the array so that the difference between the highest and
the lowest of the k scores is minimized.
Return the minimum possible difference."""

from typing import List


class Solution:
    @staticmethod
    def minDifference(nums: List[int], k: int) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(nlog(n)), Space Complexity: O(1)"""
        # Sort the scores in ascending order
        nums.sort()  # E.g. nums = [9, 4, 1, 7] -> nums = [1, 4, 7, 9]

        # Initialize the minimum difference to be the maximum possible value
        min_diff = float('inf')

        # Iterate through the scores using a sliding window of size k
        for i in range(len(nums) - k + 1):
            # Update the minimum difference between the highest and lowest scores
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff


# Unit Test: nums = [90], k = 1, Output: 0
assert Solution.minDifference([90], 1) == 0

# Unit Test: nums = [9, 4, 1, 7], k = 2, Output: 2
assert Solution.minDifference([9, 4, 1, 7], 2) == 2

# Unit Test: nums = [9, 4, 1, 7], k = 4, Output: 8
assert Solution.minDifference([9, 4, 1, 7], 4) == 8

print("All unit tests are passed.")

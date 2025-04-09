"""671. Longest Continuous Increasing Subsequence
Link: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
Difficulty: Easy
Description: Given an unsorted array of integers nums, return the length of the longest
continuous (i.e. subarray). The subarray must be strictly increasing."""

from typing import List


class Solution:
    @staticmethod
    def findLengthOfLCIS(nums: List[int]) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)"""
        # Base case: If the input array is empty
        if not nums:
            return 0

        # Initialize the variables
        n = len(nums)
        start, max_length = 0, 1

        for end in range(1, n):
            # Check if the current number is greater than the previous number
            if nums[end] > nums[end - 1]:  # Strictly increasing and continuous
                max_length = max(max_length, end - start + 1)
            else:
                start = end  # Reset the start index
        return max_length


# Input: nums = [1, 3, 5, 4, 7], Output: 3
assert Solution.findLengthOfLCIS([1, 3, 5, 4, 7]) == 3

# Input: nums = [2, 2, 2, 2, 2], Output: 1
assert Solution.findLengthOfLCIS([2, 2, 2, 2, 2]) == 1

print("All unit tests are passed.")

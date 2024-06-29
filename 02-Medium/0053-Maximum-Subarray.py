# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Description: Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
# The solution must have a time complexity of O(n).

from typing import List


class Solution:
    # Kadane's Algorithm
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        # Initialize the maximum sum and the current sum
        max_sum, current_sum = nums[0], 0
        # Sliding window: adjust the window size based on the current sum
        for n in nums:
            # If current sum is negative, ignore all the previous useless numbers and restart at 0
            current_sum = 0 if current_sum < 0 else current_sum
            # Add the current number to the current sum
            current_sum += n  # -2, 1, -2, 4, 3, 5, 6, 1, 5
            # Update the maximum sum
            max_sum = max(max_sum, current_sum)  # -2, 1, 1, 4, 4, 5, 6, 6, 6
        return max_sum


# Unit Test: Input: nums = [-2,1,-3,4,-1,2,1,-5,4], Output: 6
assert Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

# Unit Test: Input: nums = [1], Output: 1
assert Solution.maxSubArray([1]) == 1

# Unit Test: Input: nums = [5,4,-1,7,8], Output: 23
assert Solution.maxSubArray([5, 4, -1, 7, 8]) == 23

print("All unit tests are passed")

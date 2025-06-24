"""1800. Maximum Ascending Subarray Sum
Link: https://leetcode.com/problems/maximum-ascending-subarray-sum/
Difficulty: Easy
Description: Given an array of positive integers nums, return the maximum possible sum of an
ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r,
numsi  < numsi+1. Note that a subarray of size 1 is ascending."""

from typing import List


class Solution:
    @staticmethod
    def max_ascending_sum(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize variables to store the current and maximum ascending subarray sum
        current_sum = max_sum = nums[0]

        # Traverse the array and calculate the maximum ascending subarray sum
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                # Reset the current sum if the subarray is not ascending
                current_sum = nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum


# Input: nums = [10, 20, 30, 5, 10, 50], Output: 65
assert Solution.max_ascending_sum([10, 20, 30, 5, 10, 50]) == 65

# Input: nums = [10, 20, 30, 40, 50], Output: 150
assert Solution.max_ascending_sum([10, 20, 30, 40, 50]) == 150

# Input: nums = [12, 17, 15, 13, 10, 11, 12], Output: 33
assert Solution.max_ascending_sum([12, 17, 15, 13, 10, 11, 12]) == 33

print("All unit tests are passed.")

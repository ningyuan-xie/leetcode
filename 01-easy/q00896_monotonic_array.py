"""896. Monotonic Array
Link: https://leetcode.com/problems/monotonic-array/
Difficulty: Easy
Description: An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def isMonotonic(nums: List[int]) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the monotonic flag
        is_increasing = is_decreasing = True

        # Traverse the array to check if it is monotonic increasing or decreasing
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                is_increasing = False
            if nums[i] > nums[i - 1]:
                is_decreasing = False

        return is_increasing or is_decreasing


# Input: nums = [1,2,2,3], Output: True
assert Solution.isMonotonic([1, 2, 2, 3]) is True

# Input: nums = [6,5,4,4], Output: True
assert Solution.isMonotonic([6, 5, 4, 4]) is True

# Input: nums = [1,3,2], Output: False
assert Solution.isMonotonic([1, 3, 2]) is False

# Input: nums = [1,2,4,5], Output: True
assert Solution.isMonotonic([1, 2, 4, 5]) is True

# Input: nums = [1,1,1], Output: True
assert Solution.isMonotonic([1, 1, 1]) is True

print("All unit tests are passed.")

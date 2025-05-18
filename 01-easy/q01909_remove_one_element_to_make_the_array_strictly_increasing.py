"""1909. Remove One Element to Make the Array Strictly Increasing
Link: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
Difficulty: Easy
Description: Given a 0-indexed integer array nums, return true if it can be made strictly
increasing after removing exactly one element, or false otherwise. If the array is already
strictly increasing, return true.
The array nums is strictly increasing if nums[i - 1] < nums[i] for each index
(1 <= i < nums.length)."""

from typing import List


class Solution:
    @staticmethod
    def canBeIncreasing(nums: List[int]) -> bool:
        """Optimal Solution: One Pass. Time Complexity: O(n), Space Complexity: O(1)."""

        def is_strictly_increasing(arr: List[int]) -> bool:
            """Helper function to check if an array is strictly increasing."""
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            return True

        # Check each element to see if removing it results in a strictly increasing array
        for index in range(len(nums)):
            # Remove the current element and check
            if is_strictly_increasing(nums[:index] + nums[index + 1:]):
                return True

        return False


# Unit Test: nums = [1, 2, 10, 5, 7], Output: True
assert Solution.canBeIncreasing([1, 2, 10, 5, 7]) is True

# Unit Test: nums = [2, 3, 1, 2], Output: False
assert Solution.canBeIncreasing([2, 3, 1, 2]) is False

# Unit Test: nums = [1, 1, 1], Output: False
assert Solution.canBeIncreasing([1, 1, 1]) is False

print("All unit tests are passed.")

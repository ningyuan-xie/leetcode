"""747. Largest Number At Least Twice of Others
Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others
Difficulty: Easy
Description: You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other
number in the array. If it is, return the index of the largest element, or return -1 otherwise."""

from typing import List


class Solution:
    @staticmethod
    def dominant_index(nums: List[int]) -> int:
        """Optimal Solution: Two Passes. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialization: Assume the largest number is the first number
        largest_index, largest_num = 0, nums[0]

        # Pass 1: Find the largest number
        for i in range(1, len(nums)):
            # Check if the current number is greater than the largest number
            if nums[i] > largest_num:
                # If so, update the largest number and its index
                largest_index, largest_num = i, nums[i]

        # Pass 2: Check if the largest number is at least twice as much as every other number
        for i in range(len(nums)):
            # Skip the largest number
            if i != largest_index:
                # If any number is greater than half of the largest number, return -1
                if nums[i] * 2 > largest_num:
                    return -1

        # Return the index of the largest number
        return largest_index


# Unit Test: Input: nums = [3, 6, 1, 0], Output: 1
assert Solution.dominant_index([3, 6, 1, 0]) == 1

# Unit Test: Input: nums = [1, 2, 3, 4], Output: -1
assert Solution.dominant_index([1, 2, 3, 4]) == -1

# Unit Test: Input: nums = [1], Output: 0
assert Solution.dominant_index([1]) == 0

print("All unit tests are passed")

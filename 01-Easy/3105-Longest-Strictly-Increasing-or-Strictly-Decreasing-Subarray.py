"""3105. Longest Strictly Increasing or Strictly Decreasing Subarray
Link: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray
Difficulty: Easy
Description: You are given an array of integers nums. Return the length of the longest subarray of
nums which is either strictly increasing or strictly decreasing."""

from typing import List


class Solution:
    @staticmethod
    def longestMonotonicSubarray(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)"""
        max_length = 1
        current_length = 1
        increasing = True

        for i in range(1, len(nums)):
            # If the current num is the same, reset to 1
            if nums[i] == nums[i - 1]:
                current_length = 1
            # Increasing
            elif increasing and nums[i] > nums[i - 1]:
                current_length += 1
            # Decreasing
            elif not increasing and nums[i] < nums[i - 1]:
                current_length += 1
            # Switch from increasing to decreasing or vice versa, reset to 2
            else:
                increasing = not increasing
                current_length = 2

            max_length = max(max_length, current_length)

        return max_length


# Unit Test: nums = [1,4,3,3,2], Output = 2
assert Solution.longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2

# Unit Test: nums = [3,3,3,3], Output = 1
assert Solution.longestMonotonicSubarray([3, 3, 3, 3]) == 1

# Unit Test: nums = [3,2,1], Output = 3
assert Solution.longestMonotonicSubarray([3, 2, 1]) == 3

print("All unit tests are passed")

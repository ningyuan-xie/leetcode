"""2733. Neither Minimum nor Maximum
Link: https://leetcode.com/problems/neither-minimum-nor-maximum/
Difficulty: Easy
Description: Given an integer array nums containing distinct positive integers, find and return any
number from the array that is neither the minimum nor the maximum value in the array, or -1 if there
is no such number.
Return the selected integer."""

from typing import List


class Solution:
    @staticmethod
    def findNonMinOrMax(nums: List[int]) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        # Find the minimum and maximum values
        min_value = min(nums)
        max_value = max(nums)

        # Find the number that is neither the minimum nor the maximum value
        for num in nums:
            if num != min_value and num != max_value:
                return num

        return -1


# Unit Test: nums = [3,2,1,4], Output: 2 or 3
assert Solution.findNonMinOrMax([3, 2, 1, 4]) in [2, 3]

# Unit Test: nums = [1,2], Output: -1
assert Solution.findNonMinOrMax([1, 2]) == -1

# Unit Test: nums = [2,1,3], Output: 2
assert Solution.findNonMinOrMax([2, 1, 3]) == 2

print("All unit tests are passed.")

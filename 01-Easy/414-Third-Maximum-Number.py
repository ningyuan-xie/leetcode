"""414. Third Maximum Number
Link: https://leetcode.com/problems/third-maximum-number/
Difficulty: Easy
Description: Given integer array nums, return the third maximum number in this array.
If the third maximum does not exist, return the maximum number."""

from typing import List


class Solution:
    @staticmethod
    def thirdMax(nums: List[int]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)"""
        # Remove duplicates by converting the list to a set
        nums = set(nums)
        # If there are less than 3 unique numbers, return the maximum number
        if len(nums) < 3:
            return max(nums)
        # Otherwise, return the third maximum number
        # sorted(nums) returns the numbers in ascending order: [1, 2, 3]
        return sorted(nums)[-3]


# Unit Test: Input: nums = [3, 2, 1], Output: 1
assert Solution.thirdMax([3, 2, 1]) == 1

# Unit Test: Input: nums = [1, 2], Output: 2
assert Solution.thirdMax([1, 2]) == 2

# Unit Test: Input: nums = [2, 2, 3, 1], Output: 1
assert Solution.thirdMax([2, 2, 3, 1]) == 1

print("All unit tests are passed")

"""2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
Link: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
Difficulty: Easy
Description: You are given a 0-indexed array of integers nums.
A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In
particular, the prefix consisting only of nums[0] is sequential.
Return the smallest integer x missing from nums such that x is greater than or equal to the sum of
the longest sequential prefix."""

from typing import List


class Solution:
    @staticmethod
    def missingInteger(nums: List[int]) -> int:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1)"""
        # Find the sum of the longest sequential prefix
        prefix_sum = 0
        for i, num in enumerate(nums):
            if num == nums[0] + i:
                prefix_sum += num
            else:
                break

        # Find the smallest missing integer greater than or equal to the prefix sum
        missing_integer = prefix_sum
        while missing_integer in nums:
            missing_integer += 1

        return missing_integer


# Unit Test: nums = [1,2,3,2,5], Output: 6
assert Solution.missingInteger([1, 2, 3, 2, 5]) == 6

# Unit Test: nums = [3,4,5,1,12,14,13], Output: 15
assert Solution.missingInteger([3, 4, 5, 1, 12, 14, 13]) == 15

print("All unit tests are passed.")

"""908. Smallest Range I
Link: https://leetcode.com/problems/smallest-range-i/
Difficulty: Easy
Description: You are given an integer array nums and an integer k.
In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to
nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most
once for each index i.
The score of nums is the difference between the maximum and minimum elements in nums.
Return the minimum score of nums after applying the mentioned operation at most once for each
index in it."""

from typing import List


class Solution:
    @staticmethod
    def smallestRangeI(nums: List[int], k: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(n), Space Complexity: O(1)"""
        # Calculate the difference between the maximum and minimum values of nums
        diff = max(nums) - min(nums)

        # If the difference is less than 2k, return 0; otherwise, return the difference - 2k
        return max(0, diff - 2 * k)


# Input: nums = [1], k = 0, Output: 0
assert Solution.smallestRangeI([1], 0) == 0

# Input: nums = [0, 10], k = 2, Output: 6
assert Solution.smallestRangeI([0, 10], 2) == 6

# Input: nums = [1, 3, 6], k = 3, Output: 0
assert Solution.smallestRangeI([1, 3, 6], 3) == 0

print("All unit tests are passed.")

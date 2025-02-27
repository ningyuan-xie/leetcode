"""2873. Maximum Value of an Ordered Triplet I
Link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums.
Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such
triplets have a negative value, return 0.
The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k]."""

from typing import List


class Solution:
    @staticmethod
    def maximumTripletValue(nums: List[int]) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^3), Space Complexity: O(1)"""
        n = len(nums)
        max_value = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    max_value = max(max_value, (nums[i] - nums[j]) * nums[k])

        return max(max_value, 0)


# Unit Test: nums = [12,6,1,2,7], Output: 77
assert Solution.maximumTripletValue([12, 6, 1, 2, 7]) == 77

# Unit Test: nums = [1,10,3,4,19], Output: 133
assert Solution.maximumTripletValue([1, 10, 3, 4, 19]) == 133

# Unit Test: nums = [1,2,3], Output: 0
assert Solution.maximumTripletValue([1, 2, 3]) == 0

print("All unit tests are passed")

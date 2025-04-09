"""2475. Number of Unequal Triplets in Array
Link: https://leetcode.com/problems/number-of-unequal-triplets-in-array/
Difficulty: Easy
Description: You are given a 0-indexed array of positive integers nums. Find the number of triplets
(i, j, k) that meet the following conditions:
- 0 <= i < j < k < nums.length
- nums[i], nums[j], and nums[k] are pairwise distinct.
-- In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions."""

from typing import List


class Solution:
    @staticmethod
    def unequalTriplets(nums: List[int]) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^3), Space Complexity: O(1)"""
        count = 0
        n = len(nums)

        # Loop through all possible triplets (i, j, k)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if the triplet is pairwise distinct
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1
        return count


# Unit Test: nums = [4,4,2,4,3], Output: 3
assert Solution.unequalTriplets([4, 4, 2, 4, 3]) == 3

# Unit Test: nums = [1,1,1,1,1], Output: 0
assert Solution.unequalTriplets([1, 1, 1, 1, 1]) == 0

print("All unit tests are passed.")

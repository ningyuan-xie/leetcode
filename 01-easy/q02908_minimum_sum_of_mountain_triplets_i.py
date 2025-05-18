"""2908. Minimum Sum of Mountain Triplets I
Link: https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/
Difficulty: Easy
Description: You are given a 0-indexed array nums of integers.
A triplet of indices (i, j, k) is a mountain if:
- i < j < k
- nums[i] < nums[j] and nums[k] < nums[j]
Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists,
return -1."""

from typing import List


class Solution:
    @staticmethod
    def minSumOfMountainTriplets(nums: List[int]) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^3), Space Complexity: O(1)."""
        n = len(nums)
        min_sum = None

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        min_sum = nums[i] + nums[j] + nums[k] if min_sum is None else (
                            min(min_sum, nums[i] + nums[j] + nums[k]))
        return min_sum if min_sum is not None else -1


# Unit Test: nums = [8,6,1,5,3], Output: 9
assert Solution.minSumOfMountainTriplets([8, 6, 1, 5, 3]) == 9

# Unit Test: nums = [5,4,8,7,10,2], Output: 13
assert Solution.minSumOfMountainTriplets([5, 4, 8, 7, 10, 2]) == 13

# Unit Test: nums = [6,5,4,3,4,5], Output: -1
assert Solution.minSumOfMountainTriplets([6, 5, 4, 3, 4, 5]) == -1

print("All unit tests are passed.")

"""2200. Find All K-Distant Indices in an Array
Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums and two integers key and k. A k-distant
index is an index i of nums for which there exists at least one index j such that |i - j| <= k
and nums[j] == key.
Return a list of all k-distant indices sorted in increasing order."""

from typing import List


class Solution:
    @staticmethod
    def findKDistantIndices(nums: List[int], key: int, k: int) -> List[int]:
        """Optimal Solution: Brute Force. Time Complexity: O(n), Space Complexity: O(n)"""
        # Find all k-distant indices
        k_distant_indices = []
        for i in range(len(nums)):
            # Check if there exists an index j such that |i - j| <= k and nums[j] == key
            for j in range(i - k, i + k + 1):
                if 0 <= j < len(nums) and nums[j] == key:
                    k_distant_indices.append(i)
                    break
        return k_distant_indices


# Unit Test: nums = [3,4,9,1,3,9,5], key = 9, k = 1, Output: [1,2,3,4,5,6]
assert Solution.findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1) == [1, 2, 3, 4, 5, 6]

# Unit Test: nums = [2,2,2,2,2], key = 2, k = 2, Output: [0,1,2,3,4]
assert Solution.findKDistantIndices([2, 2, 2, 2, 2], 2, 2) == [0, 1, 2, 3, 4]

print("All unit tests are passed")

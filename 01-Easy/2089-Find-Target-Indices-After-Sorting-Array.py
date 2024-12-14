"""2089. Find Target Indices After Sorting Array
Link: https://leetcode.com/problems/find-target-indices-after-sorting-array
Difficulty: Easy
Description: You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order. If there
are no target indices, return an empty list. The returned list must be sorted in increasing order."""

from typing import List


class Solution:
    @staticmethod
    def findTargetIndices(nums: List[int], target: int) -> List[int]:
        """Optimal Solution: Sorting. Time Complexity: O(nlogn), Space Complexity: O(n)"""
        # Sort the list of integers
        sorted_nums = sorted(nums)  # [1, 2, 5, 2, 3] -> [1, 2, 2, 3, 5]
        # Find the indices of the target element in the sorted list
        target_indices = [i for (i, num) in enumerate(sorted_nums) if num == target]

        return target_indices


# Unit Test: nums = [1,2,5,2,3], target = 2, Output: [1, 2]
assert Solution.findTargetIndices([1, 2, 5, 2, 3], 2) == [1, 2]

# Unit Test: nums = [1,2,5,2,3], target = 3, Output: [3]
assert Solution.findTargetIndices([1, 2, 5, 2, 3], 3) == [3]

# Unit Test: nums = [1,2,5,2,3], target = 5, Output: [4]
assert Solution.findTargetIndices([1, 2, 5, 2, 3], 5) == [4]

print("All unit tests are passed")

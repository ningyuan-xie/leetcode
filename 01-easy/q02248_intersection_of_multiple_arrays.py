"""2248. Intersection of Multiple Arrays
Link: https://www.leetcode.com/problems/intersection-of-multiple-arrays/
Difficulty: Easy
Description: Given a 2D integer array nums where nums[i] is a non-empty array of distinct
positive integers, return the list of integers that are present in each array of nums sorted
in ascending order."""

from typing import List


class Solution:
    @staticmethod
    def intersection(nums: List[List[int]]) -> List[int]:
        """Optimal Solution: Set Intersection. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the result with the first set of numbers
        result = set(nums[0])  # {1, 2, 3, 4, 5}

        # For each set of numbers, compute the intersection with the result
        for i in range(1, len(nums)):
            current_set = set(nums[i])  # {1, 2, 3, 4}, {3, 4, 5, 6}
            # Retain only elements that are present in both sets
            result = {x for x in result if x in current_set}  # not using set.intersection() here

        return list(sorted(result))


# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], Output: [3,4]
assert Solution.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]) == [3, 4]

# Input: nums = [[1,2,3],[4,5,6]], Output: []
assert Solution.intersection([[1, 2, 3], [4, 5, 6]]) == []

print("All unit tests are passed.")

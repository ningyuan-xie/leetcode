"""2057. Smallest Index With Equal Value
Link: https://leetcode.com/problems/Smallest-Index-With-Equal-Value
Difficulty: Easy
Description: Given a 0-indexed integer array nums, return the smallest index i of nums such
that i mod 10 == nums[i], or -1 if such index does not exist.
x mod y denotes the remainder when x is divided by y."""

from typing import List


class Solution:
    @staticmethod
    def smallestIndex(nums: List[int]) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1


# Input: nums = [0,1,2], Output: 0
assert Solution.smallestIndex([0, 1, 2]) == 0

# Input: nums = [4,3,2,1], Output: 2
assert Solution.smallestIndex([4, 3, 2, 1]) == 2

# Input: nums = [1,2,3,4,5,6,7,8,9,0], Output: -1
assert Solution.smallestIndex([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == -1

print("All unit tests are passed.")

"""2903. Find Indices With Index and Value Difference I
Link: https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums having length n, an integer
indexDifference, and an integer valueDifference.
Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the
following conditions:
- abs(i - j) >= indexDifference, and
- abs(nums[i] - nums[j]) >= valueDifference
Return an integer array answer, where answer = [i, j] if there are two such indices, and
answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.
Note: i and j may be equal."""

from typing import List


class Solution:
    @staticmethod
    def findIndices(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(1)."""
        n = len(nums)

        for i in range(n):
            for j in range(i + indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1, -1]


# Unit Test: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4, Output: [0, 3] or [3, 0]
assert Solution.findIndices([5, 1, 4, 1], 2, 4) in [[0, 3], [3, 0]]

# Unit Test: nums = [2,1], indexDifference = 0, valueDifference = 0, Output: [0, 0]
assert Solution.findIndices([2, 1], 0, 0) == [0, 0]

# Unit Test: nums = [1,2,3], indexDifference = 2, valueDifference = 4, Output: [-1, -1]
assert Solution.findIndices([1, 2, 3], 2, 4) == [-1, -1]

print("All unit tests are passed.")

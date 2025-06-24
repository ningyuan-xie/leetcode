"""1848. Minimum Distance to the Target Element
Link: https://leetcode.com/problems/minimum-distance-to-the-target-element/
Difficulty: Easy
Description: Given an integer array nums (0-indexed) and two integers target and start, find an
index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the
absolute value of x.
Return abs(i - start).
It is guaranteed that target exists in nums."""

from typing import List


class Solution:
    @staticmethod
    def getMinDistance(nums: List[int], target: int, start: int) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the minimum distance
        min_distance = float("inf")

        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is the target
            if nums[i] == target:
                # Update the minimum distance
                min_distance = min(min_distance, abs(i - start))

        # Return the minimum distance
        return min_distance


# Input: nums = [1, 2, 3, 4, 5], target = 5, start = 3, Output: 1
assert Solution.getMinDistance([1, 2, 3, 4, 5], 5, 3) == 1

# Input: nums = [1], target = 1, start = 0, Output: 0
assert Solution.getMinDistance([1], 1, 0) == 0

print("All unit tests are passed.")

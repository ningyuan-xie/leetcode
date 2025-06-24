"""1413. Minimum Value to Get Positive Step by Step Sum
Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum
Difficulty: Easy
Description: Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in nums (from
left to right).
Return the minimum positive value of startValue such that the step by step sum is never less than 1."""

from typing import List


class Solution:
    @staticmethod
    def minStartValue(nums: List[int]) -> int:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1)."""
        min_sum, current_sum = 0, 0

        # Greedy Approach: Find the min sum during the iteration to get the min positive value
        for num in nums:
            current_sum += num  # E.g. [-3, 2, -3, 4, 2]: -3 -> -1 -> -4 -> 0 -> 2
            min_sum = min(min_sum, current_sum)  # E.g. -3 -> -3 -> -4 -> -4 -> -4
        # min positive value + min_sum = 1
        return 1 - min_sum


# Input: nums = [-3, 2, -3, 4, 2], Output: 5
assert Solution.minStartValue([-3, 2, -3, 4, 2]) == 5

# Input: nums = [1, 2], Output: 1
assert Solution.minStartValue([1, 2]) == 1

# Input: nums = [1, -2, -3], Output: 5
assert Solution.minStartValue([1, -2, -3]) == 5

print("All unit tests are passed.")

"""2656. Maximum Sum With Exactly K Elements
Link: https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums and an integer k. Your task is
to perform the following operation exactly k times in order to maximize your score:
1. Select an element m from nums.
2. Remove the selected element m from the array.
3. Add a new element with a value of m + 1 to the array.
4. Increase your score by m.
Return the maximum score you can achieve after performing the operation exactly k times."""

from typing import List


class Solution:
    @staticmethod
    def maximizeSum(nums: List[int], k: int) -> int:
        """Optimal Solution: Summation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Find the current max element in the array
        current_max = max(nums)

        # Return sum from current_max to current_max + k - 1
        return (current_max + (current_max + k - 1)) * k // 2


# Input: nums = [1,2,3,4,5], k = 3, Output: 18
assert Solution.maximizeSum([1, 2, 3, 4, 5], 3) == 18

# Input: nums = [5,5,5], k = 2, Output: 11
assert Solution.maximizeSum([5, 5, 5], 2) == 11

print("All unit tests are passed.")

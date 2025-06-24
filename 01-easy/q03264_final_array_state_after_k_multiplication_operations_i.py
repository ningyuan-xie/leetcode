"""3264. Final Array State After K Multiplication Operations I
Link: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
Difficulty: Easy
Description: You are given an integer array nums, an integer k, and an integer multiplier.
You need to perform k operations on nums. In each operation:
- Find the minimum value x in nums. If there are multiple occurrences of the minimum value, 
select the one that appears first.
- Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations."""

from typing import List


class Solution:
    @staticmethod
    def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
        """Optimal Solution: Simulation. Time Complexity: O(n * k), Space Complexity: O(1)."""
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
        return nums


# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2, Output: [8,4,6,5,6]
assert Solution.getFinalState([2, 1, 3, 5, 6], 5, 2) == [8, 4, 6, 5, 6]

# Input: nums = [1,2], k = 3, multiplier = 4, Output: [16,8]
assert Solution.getFinalState([1, 2], 3, 4) == [16, 8]

print("All unit tests are passed.")

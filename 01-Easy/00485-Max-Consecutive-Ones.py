"""485. Max Consecutive Ones
Link: https://leetcode.com/problems/max-consecutive-ones/
Difficulty: Easy
Description: Given a binary array, find the maximum number of consecutive 1s in this array."""

from typing import List


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        """Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)."""
        max_consecutive, current_consecutive = 0, 0
        for num in nums:
            if num == 1:
                current_consecutive += 1
            else:
                # Update the maximum consecutive and reset the current consecutive
                max_consecutive = max(max_consecutive, current_consecutive)
                current_consecutive = 0
        return max(max_consecutive, current_consecutive)


# Input: [1, 1, 0, 1, 1, 1], Output: 3
assert Solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3

# Input: [1, 0, 1, 1, 0, 1], Output: 2
assert Solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2

# Input: [1, 1, 1, 1, 1, 1], Output: 6
assert Solution.findMaxConsecutiveOnes([1, 1, 1, 1, 1, 1]) == 6

print("All unit tests are passed.")

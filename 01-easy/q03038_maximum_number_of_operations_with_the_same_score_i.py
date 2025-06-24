"""3038. Maximum Number of Operations With the Same Score I
Link: https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/
Difficulty: Easy
Description: You are given an array of integers nums. Consider the following operation:
- Delete the first two elements nums and define the score of the operation as the sum of
these two elements.
You can perform this operation until nums contains fewer than two elements. Additionally,
the same score must be achieved in all operations.
Return the maximum number of operations you can perform."""

from typing import List


class Solution:
    @staticmethod
    def maxOperations(nums: List[int]) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the maximum number of operations
        max_ops = 1
        score = nums.pop(0) + nums.pop(0)

        # Perform the operations and count the number of operations
        while len(nums) >= 2:
            if nums.pop(0) + nums.pop(0) == score:
                max_ops += 1
            else:
                break
        return max_ops


# Input: nums = [3,2,1,4,5], Output = 2
assert Solution.maxOperations([3, 2, 1, 4, 5]) == 2

# Input: nums = [1,5,3,3,4,1,3,2,2,3], Output = 2
assert Solution.maxOperations([1, 5, 3, 3, 4, 1, 3, 2, 2, 3]) == 2

# Input: nums = [5,3], Output = 1
assert Solution.maxOperations([5, 3]) == 1

print("All unit tests are passed.")

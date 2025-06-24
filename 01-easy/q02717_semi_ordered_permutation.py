"""2717. Semi-Ordered Permutation
Link: https://leetcode.com/problems/semi-ordered-permutation/
Difficulty: Easy
Description: You are given a 0-indexed permutation of n integers nums.
A permutation is called semi-ordered if the first number equals 1 and the last number equals n.
You can perform the below operation as many times as you want until you make nums a semi-ordered
permutation:
- Pick two adjacent elements in nums, then swap them.
Return the minimum number of operations to make nums a semi-ordered permutation.
A permutation is a sequence of integers from 1 to n of length n containing each number exactly once."""

from typing import List


class Solution:
    @staticmethod
    def semiOrderedPermutation(nums: List[int]) -> int:
        """Optimal Solution: Position Swap. Time Complexity: O(n), Space Complexity: O(1)."""
        # Find the position of 1 and n
        n = len(nums)
        position_1 = nums.index(1)
        position_n = nums.index(n)

        # Calculate the operations
        if position_1 < position_n:
            operations = position_1 + (n - 1 - position_n)
        else:
            operations = position_1 + (n - 1 - position_n) - 1

        return operations


# Input: nums = [2,1,4,3], Output: 2
assert Solution.semiOrderedPermutation([2, 1, 4, 3]) == 2

# Input: nums = [2,4,1,3], Output: 3
assert Solution.semiOrderedPermutation([2, 4, 1, 3]) == 3

# Input: nums = [1,3,4,2,5], Output: 0
assert Solution.semiOrderedPermutation([1, 3, 4, 2, 5]) == 0

print("All unit tests are passed.")

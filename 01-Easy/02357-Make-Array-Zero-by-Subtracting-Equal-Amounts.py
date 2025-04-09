"""2357. Make Array Zero by Subtracting Equal Amounts
Link: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
Difficulty: Easy
Description: You are given a non-negative integer array nums. In one operation, you must:
- Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
- Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0."""

from typing import List


class Solution:
    @staticmethod
    def minimumOperations(nums: List[int]) -> int:
        """Optimal Solution: Return the number of unique non-zero numbers in nums.
           Time Complexity: O(n), Space Complexity: O(1)"""
        return len(set([num for num in nums if num > 0]))


# Unit Test: nums = [1,5,0,3,5], Output: 3
assert Solution.minimumOperations([1, 5, 0, 3, 5]) == 3

# Unit Test: nums = [0], Output: 0
assert Solution.minimumOperations([0]) == 0

print("All unit tests are passed.")

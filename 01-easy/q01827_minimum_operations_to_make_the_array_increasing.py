"""1827. Minimum Operations to Make the Array Increasing
Link: https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
Difficulty: Easy
Description: You are given an integer array nums (0-indexed). In one operation, you can choose an
element of the array and increment it by 1.
For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.
An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An
array of length 1 is trivially strictly increasing."""

from typing import List


class Solution:
    @staticmethod
    def minOperations(nums: List[int]) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the number of operations
        operations = 0

        # Greedy approach: make each element > the previous element
        for i in range(1, len(nums)):
            # Calculate the number of operations to make the current element greater than the previous
            operations += nums[i - 1] - nums[i] + 1 if nums[i] <= nums[i - 1] else 0

            # Actually make the current element greater than the previous
            nums[i] = nums[i - 1] + 1 if nums[i] <= nums[i - 1] else nums[i]

        # Return the number of operations
        return operations


# Unit Test: nums = [1, 1, 1], Output: 3
assert Solution.minOperations([1, 1, 1]) == 3

# Unit Test: nums = [1, 5, 2, 4, 1], Output: 14
assert Solution.minOperations([1, 5, 2, 4, 1]) == 14

# Unit Test: nums = [8], Output: 0
assert Solution.minOperations([8]) == 0

print("All unit tests are passed.")

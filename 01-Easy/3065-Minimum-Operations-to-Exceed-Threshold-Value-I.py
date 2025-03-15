"""3065. Minimum Operations to Exceed Threshold Value I
Link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums, and an integer k.
In one operation, you can remove one occurrence of the smallest element of nums.
Return the minimum number of operations needed so that all elements of the array are
greater than or equal to k."""

from typing import List


class Solution:
    @staticmethod
    def minOperations(nums: List[int], k: int) -> int:
        """Optimal Solution: Count the number of elements less than k.
           Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the minimum number of operations
        ops = 0

        # Count the number of elements less than k
        for num in nums:
            if num < k:
                ops += 1
        return ops


# Unit Test: nums = [2,11,10,1,3], k = 10, Output = 3
assert Solution.minOperations([2, 11, 10, 1, 3], 10) == 3

# Unit Test: nums = [1,1,2,4,9], k = 1, Output = 0
assert Solution.minOperations([1, 1, 2, 4, 9], 1) == 0

# Unit Test: nums = [1,1,2,4,9], k = 9, Output = 4
assert Solution.minOperations([1, 1, 2, 4, 9], 9) == 4

print("All unit tests are passed")

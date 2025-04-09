"""2441. Largest Positive Integer That Exists With Its Negative
Link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
Difficulty: Easy
Description: Given an integer array nums that does not contain any zeros, find the largest positive
integer k such that -k also exists in the array.
Return the positive integer k. If there is no such integer, return -1."""

from typing import List


class Solution:
    @staticmethod
    def findMaxK(nums: List[int]) -> int:
        """Optimal Solution: Hash Set. Time Complexity: O(n), Space Complexity: O(n)"""
        # Find the largest positive integer that exists with its negative
        num_set = set(nums)
        max_k = -1

        for num in nums:
            if num > 0 and -num in num_set:
                max_k = max(max_k, num)

        return max_k


# Unit Test: nums = [-1, 2, -3, 3], Output: 3
assert Solution.findMaxK([-1, 2, -3, 3]) == 3

# Unit Test: nums = [-1, 10, 6, 7, -7, -6, 5], Output: 7
assert Solution.findMaxK([-1, 10, 6, 7, -7, -6, 5]) == 7

# Unit Test: nums = [-10, 8, 6, 7, -2, -3], Output: -1
assert Solution.findMaxK([-10, 8, 6, 7, -2, -3]) == -1

print("All unit tests are passed")

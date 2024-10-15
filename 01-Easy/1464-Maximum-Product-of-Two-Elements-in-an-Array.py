"""1464. Maximum Product of Two Elements in an Array
Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
Difficulty: Easy
Description: Given the array of integers nums, you will choose two different indices i and j of that
array. Return the maximum value of (nums[i]-1)*(nums[j]-1)."""

from typing import List


class Solution:
    @staticmethod
    def maxProduct(nums: List[int]) -> int:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(1)"""
        # Sort the nums array
        nums.sort()

        # Return the maximum product of the two largest elements in the nums array
        return (nums[-1] - 1) * (nums[-2] - 1)


# Unit Test: nums = [3, 4, 5, 2], Output: 12
assert Solution.maxProduct([3, 4, 5, 2]) == 12

# Unit Test: nums = [1, 5, 4, 5], Output: 16
assert Solution.maxProduct([1, 5, 4, 5]) == 16

# Unit Test: nums = [3, 7], Output: 12
assert Solution.maxProduct([3, 7]) == 12

# Unit Test: nums = [10, 2, 5, 2], Output: 36
assert Solution.maxProduct([10, 2, 5, 2]) == 36

print("All unit tests are passed")

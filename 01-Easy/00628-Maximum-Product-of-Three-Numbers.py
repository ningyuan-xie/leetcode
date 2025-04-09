"""628. Maximum Product of Three Numbers
Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
Difficulty: Easy
Description: Given an integer array nums, find three numbers whose product is maximum and return
the maximum product."""

from typing import List


class Solution:
    @staticmethod
    def maximumProduct(nums: List[int]) -> int:
        """Optimal Solution: Sort the array. Time Complexity: O(nlog(n)), Space Complexity: O(1)"""
        # Sort the array which takes O(nlog(n)) time
        nums.sort()
        # Product of the three largest numbers: largest if all positive
        product1 = nums[-1] * nums[-2] * nums[-3]
        # Product of the two smallest numbers and the largest number: largest if two negatives
        product2 = nums[0] * nums[1] * nums[-1]
        # The maximum product has to be one of the two cases
        return max(product1, product2)


# Input: nums = [1,2,3], Output: 6
assert Solution.maximumProduct([1, 2, 3]) == 6

# Input: nums = [1,2,3,4], Output: 24
assert Solution.maximumProduct([1, 2, 3, 4]) == 24

# Input: nums = [-1,-2,-3], Output: -6
assert Solution.maximumProduct([-1, -2, -3]) == -6

print("All unit tests are passed.")

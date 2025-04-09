"""1913. Maximum Product Difference Between Two Pairs
Link: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
Difficulty: Easy
Description: The product difference between two pairs (a, b) and (c, d) is defined as
(a * b) - (c * d).
For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product
difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
Return the maximum such product difference."""

from typing import List


class Solution:
    @staticmethod
    def maxProductDifference(nums: List[int]) -> int:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(1)"""
        nums.sort()  # Sort the array
        largest = nums[-1] * nums[-2]  # Product of two largest numbers
        smallest = nums[0] * nums[1]  # Product of two smallest numbers
        return largest - smallest

    @staticmethod
    def maxProductDifferenceLinear(nums: List[int]) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            # Find two largest: assume max1 >= max2
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num

            # Find two smallest: assume min1 <= min2
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        return (max1 * max2) - (min1 * min2)


# Unit Test: nums = [5, 6, 2, 7, 4], Output: 34
assert Solution.maxProductDifference([5, 6, 2, 7, 4]) == 34

# Unit Test: nums = [4, 2, 5, 9, 7, 4, 8], Output: 64
assert Solution.maxProductDifference([4, 2, 5, 9, 7, 4, 8]) == 64

# Unit Test: nums = [3, 4, 5, 2], Output: 14
assert Solution.maxProductDifferenceLinear([3, 4, 5, 2]) == 14

print("All unit tests are passed")

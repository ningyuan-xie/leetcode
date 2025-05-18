"""3411. Maximum Subarray With Equal Products
Link: https://leetcode.com/problems/maximum-subarray-with-equal-products/
Difficulty: Easy
Description: You are given an array of positive integers nums.
An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
• prod(arr) is the product of all elements of arr.
• gcd(arr) is the GCD of all elements of arr.
• lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums."""

from typing import List
from math import gcd, lcm


class Solution:
    @staticmethod
    def maxLength(nums: List[int]) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n^2), Space Complexity: O(1)."""
        n = len(nums)
        max_len = 0

        # Iterate through each starting index
        for i in range(n):
            g, l, p = nums[i], nums[i], nums[i]

            if p == g * l:
                max_len = max(max_len, 1)

            # Check for subarrays starting from index i
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                p *= nums[j]

                if p == g * l:
                    max_len = max(max_len, j - i + 1)

                # Break early if product is already greater than g * l
                if p > g * l:
                    break

        return max_len


def unit_tests():
    # Input: nums = [1,2,1,2,1,1,1], Output: 5
    assert Solution.maxLength([1, 2, 1, 2, 1, 1, 1]) == 5

    # Input: nums = [2,3,4,5,6], Output: 3
    assert Solution.maxLength([2, 3, 4, 5, 6]) == 3

    # Input: nums = [1,2,3,1,4,5,1], Output: 5
    assert Solution.maxLength([1, 2, 3, 1, 4, 5, 1]) == 5


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

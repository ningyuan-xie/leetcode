"""628. Maximum Product of Three Numbers
Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
Difficulty: Easy
Description: Given an integer array nums, find three numbers whose product is maximum and return the maximum product."""

from typing import List


class Solution:
    @staticmethod
    def maximumProduct(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the necessary variables
        min1 = min2 = float('inf')  # two smallest numbers
        max1 = max2 = max3 = -float('inf')  # three largest numbers

        for num in nums:
            # Update the three largest numbers
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num
            
            # Update the two smallest numbers
            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num
        
        # The maximum product is either all positive or two negatives and one positive
        return max(max1 * max2 * max3, min1 * min2 * max1)


def unit_test():
    # Input: nums = [1,2,3], Output: 6
    assert Solution.maximumProduct([1, 2, 3]) == 6

    # Input: nums = [1,2,3,4], Output: 24
    assert Solution.maximumProduct([1, 2, 3, 4]) == 24

    # Input: nums = [-1,-2,-3], Output: -6
    assert Solution.maximumProduct([-1, -2, -3]) == -6


if __name__ == "__main__":
    unit_test()
    print("All unit tests are passed.")

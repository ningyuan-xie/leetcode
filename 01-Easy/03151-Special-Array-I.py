"""3151. Special Array I
Link: https://leetcode.com/problems/special-array-I
Difficulty: Easy
Description: An array is considered special if the parity of every pair of adjacent elements is
different. In other words, one element in each pair must be even, and the other must be odd.
You are given an array of integers nums. Return true if nums is a special array, otherwise,
return false."""

from typing import List


class Solution:
    @staticmethod
    def isArraySpecial(nums: List[int]) -> bool:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the length of the array
        n = len(nums)

        # Iterate through the array
        for i in range(n - 1):
            # Check if the parity of adjacent elements is the same
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        # If all adjacent elements have different parity, return True
        return True


# Unit Test: nums = [1], Output = True
assert Solution.isArraySpecial([1]) is True

# Unit Test: nums = [2,1,4], Output = True
assert Solution.isArraySpecial([2, 1, 4]) is True

# Unit Test: nums = [4,3,1,6], Output = False
assert Solution.isArraySpecial([4, 3, 1, 6]) is False

print("All unit tests are passed.")

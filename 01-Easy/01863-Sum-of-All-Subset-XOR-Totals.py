"""1863. Sum of All Subset XOR Totals
Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
Difficulty: Easy
Description: The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if
the array is empty.
- For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.
Note: Subsets with the same elements should be counted multiple times.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero)
elements of b."""

from typing import List


class Solution:
    @staticmethod
    def subsetXORSum(nums: List[int]) -> int:
        """Optimal Solution: Backtracking. Time Complexity: O(2^n), Space Complexity: O(n).
           Bitwise XOR operator ^ : 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0"""

        def backtrack(index: int, current_xor: int) -> int:
            """Helper function to backtrack through all subsets and calculate the XOR total"""
            # Base case: If we've considered all elements
            if index == len(nums):
                return current_xor  # Return the XOR of this subset

            # Recursive case: Include the current element in the subset; XOR with the current element
            include = backtrack(index + 1, current_xor ^ nums[index])

            # Recursive case: Exclude the current element in the subset; current XOR remains the same
            exclude = backtrack(index + 1, current_xor)

            # Return the sum of XORs of both cases
            return include + exclude

        # Start backtracking with index 0 and an initial XOR of 0
        return backtrack(0, 0)


# Unit Test: nums = [1, 3], Output: 6
assert Solution.subsetXORSum([1, 3]) == 6

# Unit Test: nums = [5, 1, 6], Output: 28
assert Solution.subsetXORSum([5, 1, 6]) == 28

print("All unit tests are passed")

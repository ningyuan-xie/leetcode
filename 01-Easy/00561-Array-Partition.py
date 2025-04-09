"""561. Array Partition I
Link: https://leetcode.com/problems/array-partition/
Difficulty: Easy
Description: Given an integer array nums of 2n integers, group these integers into
n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
Return the maximized sum."""

from typing import List


class Solution:
    @staticmethod
    def arrayPairSum(nums: List[int]) -> int:
        """Optimal Solution: Sort and Sum. Time Complexity: O(nlog(n)), Space Complexity: O(1).
           Sort the array in ascending order: This ensures that when we form pairs, the smallest ones
           are always paired with the next smallest ones, so we don't waste the bigger ones"""
        nums.sort()  # [1, 4, 3, 2] -> [1, 2, 3, 4]. .sort() takes O(nlog(n)) because divide & conquer
        # Initialize the sum variable
        sum_min_pairs = 0
        # Iterate through the sorted array by 2
        for i in range(0, len(nums), 2):
            # Sum the minimum of each pair: min(1, 2) + min(3, 4) = 1 + 3 = 4
            sum_min_pairs += nums[i]
        return sum_min_pairs


# Input: nums = [1, 4, 3, 2], Output: 4
assert Solution.arrayPairSum([1, 4, 3, 2]) == 4

# Input: nums = [6, 2, 6, 5, 1, 2], Output: 9
assert Solution.arrayPairSum([6, 2, 6, 5, 1, 2]) == 9

print("All unit tests are passed.")

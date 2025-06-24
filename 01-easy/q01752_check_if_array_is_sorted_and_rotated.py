"""1752. Check if Array Is Sorted and Rotated
Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
Difficulty: Easy
Description: Given an array nums, return true if the array was originally sorted in non-decreasing
order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that
A[i] == B[(i+x) % A.length], where % is the modulo operation."""

from typing import List


class Solution:
    @staticmethod
    def check(nums: List[int]) -> bool:
        """Optimal Solution: Rotations. Time Complexity: O(n), Space Complexity: O(1).
           The main idea is to detect points in the array where an element is greater than the
           next one, indicating a descending transition. In a sorted rotated array, at most one
           such descending transition is allowed"""
        # Iterate through the array to detect descending transitions
        rotations = 0

        # Check if the current element is greater than the next element;
        # using modulo ensures that the last element is compared with the first element
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                # Increment the rotation counter if a descending transition is found
                rotations += 1

        # The array is considered sorted and rotated if there's at most one descending transition
        return rotations <= 1


# Input: nums = [3, 4, 5, 1, 2], Output: True
assert Solution.check([3, 4, 5, 1, 2]) is True

# Input: nums = [2, 1, 3, 4], Output: False
assert Solution.check([2, 1, 3, 4]) is False

# Input: nums = [1, 2, 3], Output: True
assert Solution.check([1, 2, 3]) is True

print("All unit tests are passed.")

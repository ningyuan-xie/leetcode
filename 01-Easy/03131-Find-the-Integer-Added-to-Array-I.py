"""3131. Find the Integer Added to Array I
Link: https://leetcode.com/problems/find-the-integer-added-to-array-i
Difficulty: Easy
Description: You are given two arrays of equal length, nums1 and nums2.
Each element in nums1 has been increased (or decreased in the case of negative) by an integer,
represented by the variable x.
As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the
same integers with the same frequencies.
Return the integer x."""

from typing import List


class Solution:
    @staticmethod
    def addedInteger(nums1: List[int], nums2: List[int]) -> int:
        """Optimal Solution: Math. Time Complexity: O(n), Space Complexity: O(1)"""
        return min(nums2) - min(nums1)


# Unit Test: nums1 = [2,6,4], nums2 = [9,7,5], Output = 3
assert Solution.addedInteger([2, 6, 4], [9, 7, 5]) == 3

# Unit Test: nums1 = [10], nums2 = [5], Output = -5
assert Solution.addedInteger([10], [5]) == -5

# Unit Test: nums1 = [1,1,1,1], nums2 = [1,1,1,1], Output = 0
assert Solution.addedInteger([1, 1, 1, 1], [1, 1, 1, 1]) == 0

print("All unit tests are passed")

"""2540. Minimum Common Value
Link: https://leetcode.com/problems/minimum-common-value/
Difficulty: Easy
Description: Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the
minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one
occurrence of that integer."""

from typing import List


class Solution:
    @staticmethod
    def getCommon(nums1: List[int], nums2: List[int]) -> int:
        """Optimal Solution: Set Intersection. Time Complexity: O(n), Space Complexity: O(n)."""
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1.intersection(set2)

        # Return the minimum common value
        return min(common) if common else -1


# Unit Test: nums1 = [1,2,3], nums2 = [2,4], Output: 2
assert Solution.getCommon([1, 2, 3], [2, 4]) == 2

# Unit Test: nums1 = [1,2,3,6], nums2 = [2,3,4,5], Output: 2
assert Solution.getCommon([1, 2, 3, 6], [2, 3, 4, 5]) == 2

print("All unit tests are passed.")

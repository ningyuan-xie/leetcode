"""349. Intersection of Two Arrays
Link: https://leetcode.com/problems/intersection-of-two-arrays/
Difficulty: Easy
Description: Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order."""

from typing import List


class Solution:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        """Optimal Solution: Two Sets. Time Complexity: O(n + m), Space Complexity: O(n + m)"""
        # Initialize two sets to store the unique elements of nums1 and nums2
        set1, set2 = set(nums1), set(nums2)
        # Initialize a list to store the intersection of nums1 and nums2
        intersection = []
        for num in set1:
            # If the element is in set2, add it to the intersection
            if num in set2:
                intersection.append(num)
        return intersection


# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2], Output: [2]
assert Solution.intersection([1, 2, 2, 1], [2, 2]) == [2]

# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4], Output: [9, 4]
assert Solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]

print("All unit tests are passed.")

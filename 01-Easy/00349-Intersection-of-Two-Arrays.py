"""349. Intersection of Two Arrays
Link: https://leetcode.com/problems/intersection-of-two-arrays/
Difficulty: Easy
Description: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order."""

from typing import List


class Solution:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        """Optimal Solution: Set. Time Complexity: O(n + m), Space Complexity: O(n)."""
        # Convert nums1 to a set to remove duplicates and allow for O(1) lookups
        set_nums1 = set(nums1)
        # Use a set comprehension to find the intersection with nums2
        return list({num for num in nums2 if num in set_nums1})


def unit_tests():
    # Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2], Output: [2]
    assert Solution.intersection([1, 2, 2, 1], [2, 2]) == [2]

    # Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4], Output: [9, 4]
    assert Solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""2215. Find the Difference of Two Arrays
Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/
Difficulty: Easy
Description: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2
where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order."""

from typing import List


class Solution:
    @staticmethod
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """Optimal Solution: List & Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # Convert to set for faster lookup
        set1, set2 = set(nums1), set(nums2)

        # Find elements in nums1 not in nums2 and vice versa
        diff1 = [num for num in set1 if num not in set2]
        diff2 = [num for num in set2 if num not in set1]
        return [diff1, diff2]


# Input: nums1 = [1,2,3], nums2 = [2,4,6], Output: [[1,3],[4,6]]
assert Solution.findDifference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]]

# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2], Output: [[3],[]]
assert Solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2]) == [[3], []]

# Input: nums1 = [-68,-80,-19,-94,82,21,-43], nums2 = [-63],
# Output: [[-94, -19, -80, 82, 21, -43, -68],[-63]]
assert (Solution.findDifference([-68, -80, -19, -94, 82, 21, -43], [-63])
        == [[-94, -19, -80, 82, 21, -43, -68], [-63]])

print("All unit tests are passed.")

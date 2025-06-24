"""2956. Find Common Elements Between Two Arrays
Link: https://leetcode.com/problems/find-common-elements-between-two-arrays/
Difficulty: Easy
Description: You are given two integer arrays nums1 and nums2 of sizes n and m, respectively.
Calculate the following values:
- answer1 : the number of indices i such that nums1[i] exists in nums2.
- answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2]."""

from typing import List


class Solution:
    @staticmethod
    def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        answer1 = sum(1 for num in nums1 if num in nums2)
        answer2 = sum(1 for num in nums2 if num in nums1)

        return [answer1, answer2]


# Input: nums1 = [2,3,2], nums2 = [1,2], Output: [2,1]
assert Solution.findIntersectionValues([2, 3, 2], [1, 2]) == [2, 1]

# Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6], Output: [3,4]
assert Solution.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]) == [3, 4]

# Input: nums1 = [3,4,2,3], nums2 = [1,5], Output: [0,0]
assert Solution.findIntersectionValues([3, 4, 2, 3], [1, 5]) == [0, 0]

print("All unit tests are passed.")

"""2605. Form Smallest Number From Two Digit Arrays
Link: https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/
Difficulty: Easy
Description: Given two arrays of unique digits nums1 and nums2, return the smallest number that
contains at least one digit from each array."""

from typing import List


class Solution:
    @staticmethod
    def minNumber(nums1: List[int], nums2: List[int]) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(n), Space Complexity: O(1)."""
        # Sort both arrays in ascending order
        nums1.sort()  # [4, 1, 3] -> [1, 3, 4]
        nums2.sort()  # [5, 7] -> [5, 7]

        # Iterate through the sorted arrays to find the smallest common digit
        for i in nums1:
            for j in nums2:
                if i == j:
                    return i

        # If no common digit is found,
        # return the smallest number formed by the smallest digits from both arrays
        return min(nums1[0] * 10 + nums2[0], nums2[0] * 10 + nums1[0])


# Input: arr1 = [4, 1, 3], arr2 = [5, 7], Output: 15
assert Solution.minNumber([4, 1, 3], [5, 7]) == 15

# Input: nums1 = [3, 5, 2, 6], nums2 = [3, 1, 7], Output: 3
assert Solution.minNumber([3, 5, 2, 6], [3, 1, 7]) == 3

print("All unit tests are passed.")

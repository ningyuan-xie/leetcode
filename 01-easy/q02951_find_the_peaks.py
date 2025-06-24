"""2951. Find the Peaks
Link: https://leetcode.com/problems/find-the-peaks/
Difficulty: Easy
Description: You are given a 0-indexed array mountain. Your task is to find all the peaks in
the mountain array.
Return an array that consists of indices of peaks in the given array in any order.
Notes:
- A peak is defined as an element that is strictly greater than its neighboring elements.
- The first and last elements of the array are not a peak."""

from typing import List


class Solution:
    @staticmethod
    def findPeaks(mountain: List[int]) -> List[int]:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(mountain)
        peaks = []

        # Iterate through each element in the mountain array
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)

        return peaks


# Input: mountain = [2,4,4], Output: []
assert Solution.findPeaks([2, 4, 4]) == []

# Input: mountain = [1,4,3,8,5], Output: [1,3]
assert Solution.findPeaks([1, 4, 3, 8, 5]) == [1, 3]

print("All unit tests are passed.")

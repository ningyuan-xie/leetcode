"""1287. Element Appearing More Than 25% In Sorted Array
Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
Difficulty: Easy
Description: Given an integer array sorted in non-decreasing order, there is an integer in the array
that occurs more than 25% of the time. Return that integer."""

from typing import List


class Solution:
    @staticmethod
    def findSpecialInteger(arr: List[int]) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the window size as 25% of the array length
        window_size = len(arr) // 4

        # Initialize the left and right pointers
        left, right = 0, window_size

        # Slide the window
        while right < len(arr):
            # Check if the current window is the answer
            if arr[left] == arr[right]:
                return arr[left]

            # Slide the window
            left += 1
            right += 1

        # Given that the array is sorted and the requirement is that a number appears more than 25%
        # of the time, the last element will always be the answer if no earlier match is found
        return arr[-1]


# Unit Test: arr = [1, 2, 2, 6, 6, 6, 6, 7, 10], Output: 6
assert Solution.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6

# Unit Test: arr = [1, 1], Output: 1
assert Solution.findSpecialInteger([1, 1]) == 1

print("All unit tests are passed.")

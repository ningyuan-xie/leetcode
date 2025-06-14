"""941. Valid Mountain Array
Link: https://leetcode.com/problems/valid-mountain-array/
Difficulty: Easy
Description: Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
• arr.length >= 3
• There exists some i with 0 < i < arr.length - 1 such that:
  • arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
  • arr[i] > arr[i + 1] > ... > arr[arr.length - 1]"""

from typing import List


class Solution:
    @staticmethod
    def validMountainArray(arr: List[int]) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the left and right pointers
        left, right = 0, len(arr) - 1

        # Move the left pointer to the right until it reaches the peak
        while left < right and arr[left] < arr[left + 1]:
            left += 1

        # Move the right pointer to the left until it reaches the peak
        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1

        # Return True if the left and right pointers meet at the peak
        return 0 < left == right < len(arr) - 1


def unit_tests():
    # Input: [2,1], Output: False
    assert Solution.validMountainArray([2, 1]) is False

    # Input: [3,5,5], Output: False
    assert Solution.validMountainArray([3, 5, 5]) is False

    # Input: [0,3,2,1], Output: True
    assert Solution.validMountainArray([0, 3, 2, 1]) is True

    # Input: [0,1,2,3,4,5,6,7,8,9], Output: False
    assert Solution.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) is False

    # Input: [9,8,7,6,5,4,3,2,1,0], Output: False
    assert Solution.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) is False

    # Input: [0,1,2,3,4,5,4,3,2,1,0], Output: True
    assert Solution.validMountainArray([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

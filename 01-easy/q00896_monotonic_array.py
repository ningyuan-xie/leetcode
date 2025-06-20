"""896. Monotonic Array
Link: https://leetcode.com/problems/monotonic-array/
Difficulty: Easy
Description: An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def isMonotonic(nums: List[int]) -> bool:
        """Optimal Solution: One Pass with Early Termination. Time Complexity: O(n), Space Complexity: O(1)."""
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            elif nums[i] < nums[i-1]:
                increasing = False
                
            # Early termination if both flags are False
            if not increasing and not decreasing:
                return False
                
        return increasing or decreasing


def unit_tests():
    # Input: nums = [1,2,2,3], Output: True
    assert Solution.isMonotonic([1, 2, 2, 3]) is True

    # Input: nums = [6,5,4,4], Output: True
    assert Solution.isMonotonic([6, 5, 4, 4]) is True

    # Input: nums = [1,3,2], Output: False
    assert Solution.isMonotonic([1, 3, 2]) is False

    # Input: nums = [1,2,4,5], Output: True
    assert Solution.isMonotonic([1, 2, 4, 5]) is True

    # Input: nums = [1,1,1], Output: True
    assert Solution.isMonotonic([1, 1, 1]) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

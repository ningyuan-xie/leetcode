"""747. Largest Number At Least Twice of Others
Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others
Difficulty: Easy
Description: You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise."""

from typing import List


class Solution:
    @staticmethod
    def dominant_index(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        largest = max(nums)
        for num in nums:
            if num != largest and num * 2 > largest:
                return -1
        # Return the index of the largest number
        return nums.index(largest)


def unit_tests():
    # Input: nums = [3, 6, 1, 0], Output: 1
    assert Solution.dominant_index([3, 6, 1, 0]) == 1

    # Input: nums = [1, 2, 3, 4], Output: -1
    assert Solution.dominant_index([1, 2, 3, 4]) == -1

    # Input: nums = [1], Output: 0
    assert Solution.dominant_index([1]) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

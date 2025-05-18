"""643. Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/
Difficulty: Easy
Description: You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted."""

from typing import List


class Solution:
    @staticmethod
    def findMaxAverage(nums: List[int], k: int) -> float:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize window sum with first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide window through the array
        for i in range(k, len(nums)):
            # Add new element and remove oldest element
            window_sum += nums[i] - nums[i - k]
            # Update max_sum if current window is larger
            if window_sum > max_sum:
                max_sum = window_sum
                
        return max_sum / k


def unit_tests():
    # Input: nums = [1, 12, -5, -6, 50, 3], k = 4, Output: 12.75 = (12 - 5 - 6 + 50) / 4
    assert Solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75

    # Input: nums = [5], k = 1, Output: 5.0
    assert Solution.findMaxAverage([5], 1) == 5.0

    # Input: nums = [0, 1, 1, 3, 3], k = 4, Output: 2.0
    assert Solution.findMaxAverage([0, 1, 1, 3, 3], 4) == 2.0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""671. Longest Continuous Increasing Subsequence
Link: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
Difficulty: Easy
Description: Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1]."""

from typing import List


class Solution:
    @staticmethod
    def findLengthOfLCIS(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the maximum length and current length
        max_len = curr_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1
                
        return max_len


def unit_tests():
    # Input: nums = [1, 3, 5, 4, 7], Output: 3
    assert Solution.findLengthOfLCIS([1, 3, 5, 4, 7]) == 3

    # Input: nums = [2, 2, 2, 2, 2], Output: 1
    assert Solution.findLengthOfLCIS([2, 2, 2, 2, 2]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

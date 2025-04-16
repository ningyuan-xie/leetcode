"""3427. Sum of Variable-Length Subarrays
Link: https://leetcode.com/problems/sum-of-variable-length-subarrays/
Difficulty: Easy
Description: You are given an integer array nums of size n. For each index i where 0 <= i < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).
Return the total sum of all elements from the subarray defined for each index in the array."""

from typing import List


class Solution:
    @staticmethod
    def subarraySum(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(nums)
        total_sum = 0

        for i in range(n):
            start = max(0, i - nums[i])
            total_sum += sum(nums[start:i + 1])

        return total_sum


def unit_tests():
    # Input: nums = [2,3,1], Output: 11
    assert Solution.subarraySum([2, 3, 1]) == 11

    # Input: nums = [3,1,1,2], Output: 13
    assert Solution.subarraySum([3, 1, 1, 2]) == 13


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

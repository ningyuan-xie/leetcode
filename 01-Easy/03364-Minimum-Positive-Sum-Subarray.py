"""3364. Minimum Positive Sum Subarray
Link: https://leetcode.com/problems/minimum-positive-sum-subarray/
Difficulty: Easy
Description: You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.
Return the minimum sum of such a subarray. If no such subarray exists, return -1.
A subarray is a contiguous non-empty sequence of elements within an array."""

from typing import List


class Solution:
    @staticmethod
    def minimumSumSubarray(nums: List[int], l: int, r: int) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(1)."""
        n = len(nums)
        min_sum = float('inf')

        # Iterate through all possible subarrays
        for i in range(n):
            current_sum = 0
            # Check subarrays of size l to r
            for j in range(i, min(i + r, n)):
                current_sum += nums[j]
                if j - i + 1 >= l and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
        
        return min_sum if min_sum != float('inf') else -1


def unit_tests():
    # Input: nums = [3, -2, 1, 4], l = 2, r = 3, Output: 1
    assert Solution.minimumSumSubarray([3, -2, 1, 4], 2, 3) == 1

    # Input: nums = [-2, 2, -3, 1], l = 2, r = 3, Output: -1
    assert Solution.minimumSumSubarray([-2, 2, -3, 1], 2, 3) == -1

    # Input: nums = [1, 2, 3, 4], l = 2, r = 4, Output: 3
    assert Solution.minimumSumSubarray([1, 2, 3, 4], 2, 4) == 3

    # Input: nums = [17, 13], l = 1, r = 2, Output: 13
    assert Solution.minimumSumSubarray([17, 13], 1, 2) == 13

    # Input: nums = [-3,17], l = 1, r = 2, Output: 17
    assert Solution.minimumSumSubarray([-3, 17], 1, 2) == 14

    # Input: nums = [-23,2,-12], l = 1, r = 2, Output: 2
    assert Solution.minimumSumSubarray([-23, 2, -12], 1, 2) == 2


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

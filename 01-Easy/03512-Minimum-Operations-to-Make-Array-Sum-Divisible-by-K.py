"""3512. Minimum Operations to Make Array Sum Divisible by K
Link: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
Difficulty: Easy
Description: You are given an integer array nums and an integer k. You can perform the following operation any number of times:
• Select an index i and replace nums[i] with nums[i] - 1.
Return the minimum number of operations required to make the sum of the array divisible by k."""

from typing import List


class Solution:
    @staticmethod
    def minOperations(nums: List[int], k: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        return sum(nums) % k


def unit_tests():
    # Input: nums = [3,9,7], k = 5, Output: 4
    assert Solution.minOperations([3, 9, 7], 5) == 4

    # Input: nums = [4,1,3], k = 4, Output: 0
    assert Solution.minOperations([4, 1, 3], 4) == 0

    # Input: nums = [3,2], k = 6, Output: 5
    assert Solution.minOperations([3, 2], 6) == 5


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

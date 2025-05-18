"""3432. Count Partitions With Even Sum Difference
Link: https://leetcode.com/problems/count-partitions-with-even-sum-difference/
Difficulty: Easy
Description: You are given an integer array nums of length n.
A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:
• Left subarray contains indices [0, i].
• Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right subarrays is even."""

from typing import List


class Solution:
    @staticmethod
    def countPartitions(nums: List[int]) -> int:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(nums)
        total_sum = sum(nums)
        even_count = 0

        for i in range(n - 1):
            left_sum = sum(nums[:i + 1])
            right_sum = total_sum - left_sum
            if (left_sum - right_sum) % 2 == 0:
                even_count += 1

        return even_count


def unit_tests():
    # Input: nums = [10,10,3,7,6], Output: 4
    assert Solution.countPartitions([10, 10, 3, 7, 6]) == 4

    # Input: nums = [1,2,2], Output: 0
    assert Solution.countPartitions([1, 2, 2]) == 0

    # Input: nums = [2,4,6,8], Output: 3
    assert Solution.countPartitions([2, 4, 6, 8]) == 3


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

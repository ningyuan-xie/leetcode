"""3392. Count Subarrays of Length Three With a Condition
Link: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
Difficulty: Easy
Description: Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number."""

from typing import List


class Solution:
    @staticmethod
    def countSubarrays(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        count = 0
        n = len(nums)

        for i in range(1, n - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                count += 1

        return count


def unit_tests():
    # Input: nums = [1,2,1,4,1], Output: 1
    assert Solution.countSubarrays([1, 2, 1, 4, 1]) == 1

    # Input: nums = [1,1,1], Output: 0
    assert Solution.countSubarrays([1, 1, 1]) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

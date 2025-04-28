"""268. Missing Number
Link: https://leetcode.com/problems/missing-number/
Difficulty: Easy
Description: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""

from typing import List


class Solution:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        """Optimal Solution: Gauss's Formula. Time Complexity: O(n), Space Complexity: O(1)."""
        # Calculate the expected sum of numbers from 0 to n
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        
        return expected_sum - sum(nums)


def unit_tests():
    # Input: nums = [3,0,1], Output: 2
    assert Solution.missingNumber([3, 0, 1]) == 2

    # Input: nums = [0,1], Output: 2
    assert Solution.missingNumber([0, 1]) == 2  # 2 ^ (0 ^ 2) ^ (1 ^ 0) = 2

    # Input: nums = [9,6,4,2,3,5,7,0,1], Output: 8
    assert Solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

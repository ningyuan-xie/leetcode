"""136. Single Number
Link: https://leetcode.com/problems/single-number/
Difficulty: Easy
Description: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space."""

from typing import List


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(n), Space Complexity: O(1).
           0 ^ 0 = 0, 0 ^ 1 = 1, 1 ^ 1 = 0."""
        # Initialize the result to 0
        result = 0

        # Iterate through the numbers in the array
        for num in nums:
            # Apply XOR operation
            result ^= num

        return result


def unit_tests():
    # Input: nums = [2,2,1], Output: 1
    assert Solution.singleNumber([2, 2, 1]) == 1

    # Input: nums = [4,1,2,1,2], Output: 4
    assert Solution.singleNumber([4, 1, 2, 1, 2]) == 4

    # Input: nums = [1], Output: 1
    assert Solution.singleNumber([1]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

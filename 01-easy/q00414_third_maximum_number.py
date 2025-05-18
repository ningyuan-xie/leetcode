"""414. Third Maximum Number
Link: https://leetcode.com/problems/third-maximum-number/
Difficulty: Easy
Description: Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number."""

from typing import List


class Solution:
    @staticmethod
    def thirdMax(nums: List[int]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)."""
        # Create a set to store distinct numbers
        distinct_nums = set(nums)

        # If there are less than 3 distinct numbers, return the maximum
        if len(distinct_nums) < 3:
            return max(distinct_nums)

        # Remove the maximum number twice to get the third maximum
        distinct_nums.remove(max(distinct_nums))
        distinct_nums.remove(max(distinct_nums))

        return max(distinct_nums)


def unit_tests():
    # Input: nums = [3, 2, 1], Output: 1
    assert Solution.thirdMax([3, 2, 1]) == 1

    # Input: nums = [1, 2], Output: 2
    assert Solution.thirdMax([1, 2]) == 2

    # Input: nums = [2, 2, 3, 1], Output: 1
    assert Solution.thirdMax([2, 2, 3, 1]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

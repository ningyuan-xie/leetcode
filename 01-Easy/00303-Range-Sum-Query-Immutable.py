"""303. Range Sum Query - Immutable
Link: https://leetcode.com/problems/range-sum-query-immutable/
Difficulty: Easy
Description: Given an integer array nums, handle multiple queries of the following type:
1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
• NumArray(int[] nums) Initializes the object with the integer array nums.
• int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right])."""

from typing import List


class NumArray:
    """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(n)."""

    def __init__(self, nums: List[int]):
        """Constructor: Initialize the prefix sum array to store the sum of the elements of nums."""
        self.prefix_sum = []
        current_sum = 0
        
        # Fill the prefix sum array with the sum of the elements of nums
        for num in nums:
            current_sum += num
            self.prefix_sum.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        """sumRange: Calculate the sum of the elements of nums between indices left and right inclusive."""
        left_sum = self.prefix_sum[left - 1] if left > 0 else 0
        right_sum = self.prefix_sum[right]
        return right_sum - left_sum


def unit_tests():
    # Input: ["NumArray", "sumRange", "sumRange", "sumRange"], [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]], Output: [null, 1, -1, -3]
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    assert num_array.sumRange(0, 2) == 1
    assert num_array.sumRange(2, 5) == -1
    assert num_array.sumRange(0, 5) == -3


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

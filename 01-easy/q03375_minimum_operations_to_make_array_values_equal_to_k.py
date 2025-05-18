"""3375. Minimum Operations to Make Array Values Equal to K
Link: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
Difficulty: Easy
Description: You are given an integer array nums and an integer k.
An integer h is called valid if all values in the array that are strictly greater than h are identical.
For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.
You are allowed to perform the following operation on nums:
• Select an integer h that is valid for the current values in nums.
• For each index i where nums[i] > h, set nums[i] to h.
Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1."""

from typing import List


class Solution:
    @staticmethod
    def minOperations(nums: List[int], k: int) -> int:
        """Optimal Solution: Hash Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # If any value is less than k, it cannot be increased, so return -1
        if any(num < k for num in nums):
            return -1

        # Keep only numbers greater than k
        above_k = [num for num in nums if num > k]

        # Count the number of segments of identical values above k
        return len(set(above_k))


def unit_tests():
    # Input: nums = [5,2,5,4,5], k = 2, Output: 2
    assert Solution.minOperations([5, 2, 5, 4, 5], 2) == 2

    # Input: nums = [2,1,2], k = 2, Output: -1
    assert Solution.minOperations([2, 1, 2], 2) == -1

    # Input: nums = [9,7,5,3], k = 1, Output: 4
    assert Solution.minOperations([9, 7, 5, 3], 1) == 4


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

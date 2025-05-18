"""3487. Maximum Unique Subarray Sum After Deletion
Link: https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
Difficulty: Easy
Description: You are given an integer array nums.
You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:
1. All elements in the subarray are unique.
2. The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray."""

from typing import List


class Solution:
    @staticmethod
    def maxSum(nums: List[int]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # If the maximum element in the array is less than zero, the answer is the maximum element
        if max(nums) < 0:
            return max(nums)
        
        # Otherwise, the answer is the sum of all unique values that are greater than or equal to zero
        unique_elements = set()
        for num in nums:
            if num >= 0:
                unique_elements.add(num)
        return sum(unique_elements)


def unit_tests():
    # Input: nums = [1,2,3,4,5], Output: 15
    assert Solution.maxSum([1, 2, 3, 4, 5]) == 15

    # Input: nums = [1,1,0,1,1], Output: 1
    assert Solution.maxSum([1, 1, 0, 1, 1]) == 1

    # Input: nums = [1,2,-1,-2,1,0,-1], Output: 3
    assert Solution.maxSum([1, 2, -1, -2, 1, 0, -1]) == 3


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""724. Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/
Difficulty: Easy
Description: Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the
index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no
elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1."""

from typing import List


class Solution:
    @staticmethod
    def pivot_index(nums: List[int]) -> int:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1)."""
        # Compute the total sum of the array
        total_sum = sum(nums)

        # Initialize the left sum to 0
        left_sum = 0

        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if the left sum == right sum
            if left_sum == total_sum - left_sum - num:
                # If so, return the index
                return i
            else:
                # Update the left sum
                left_sum += num

        # If no pivot index is found, return -1
        return -1


# Input: nums = [1, 7, 3, 6, 5, 6], Output: 3
assert Solution.pivot_index([1, 7, 3, 6, 5, 6]) == 3

# Input: nums = [1, 2, 3], Output: -1
assert Solution.pivot_index([1, 2, 3]) == -1

# Input: nums = [2, 1, -1], Output: 0
assert Solution.pivot_index([2, 1, -1]) == 0

print("All unit tests are passed.")

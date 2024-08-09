"""704. Binary Search
Link: https://leetcode.com/problems/binary-search/
Difficulty: Easy
Description: Given an array of integers nums which is sorted in ascending order, and an integer
target, write a function to search target in nums."""

from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)"""
        # Initialize the two pointers
        left, right = 0, len(nums) - 1

        # Iterate through the list of numbers
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # If the target is found, return the index
            if nums[mid] == target:
                return mid
            # If the target is less than the middle element, move the right pointer
            elif target < nums[mid]:
                right = mid - 1
            # If the target is greater than the middle element, move the left pointer
            else:
                left = mid + 1

        # If the target is not found, return -1
        return -1


# Unit Test: Input: nums = [-1, 0, 3, 5, 9, 12], target = 9, Output: 4
assert Solution.search([-1, 0, 3, 5, 9, 12], 9) == 4

# Unit Test: Input: nums = [-1, 0, 3, 5, 9, 12], target = 2, Output: -1
assert Solution.search([-1, 0, 3, 5, 9, 12], 2) == -1

# Unit Test: Input: nums = [5], target = 5, Output: 0
assert Solution.search([5], 5) == 0

print("All unit tests are passed")

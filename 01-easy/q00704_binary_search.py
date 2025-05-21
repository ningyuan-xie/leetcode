"""704. Binary Search
Link: https://leetcode.com/problems/binary-search/
Difficulty: Easy
Description: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity."""

from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


def unit_tests():
    # Input: nums = [-1, 0, 3, 5, 9, 12], target = 9, Output: 4
    assert Solution.search([-1, 0, 3, 5, 9, 12], 9) == 4

    # Input: nums = [-1, 0, 3, 5, 9, 12], target = 2, Output: -1
    assert Solution.search([-1, 0, 3, 5, 9, 12], 2) == -1

    # Input: nums = [5], target = 5, Output: 0
    assert Solution.search([5], 5) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

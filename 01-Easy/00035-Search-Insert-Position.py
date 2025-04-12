"""35. Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy
Description: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity."""

from typing import List


class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2

            # If the target is found, return the index
            if nums[mid] == target:
                return mid
            # If the target is less than the middle element, search in the left half
            elif nums[mid] > target:
                right = mid - 1
            # If the target is greater than the middle element, search in the right half
            else:
                left = mid + 1
        # After the loop ends, left is the first index where nums[left] >= target.
        return left


def unit_tests():
    # Input: nums = [1, 3, 5, 6], target = 5, Output: 2
    assert Solution.searchInsert([1, 3, 5, 6], 5) == 2

    # Input: nums = [1, 3, 5, 6], target = 2, Output: 1
    assert Solution.searchInsert([1, 3, 5, 6], 2) == 1

    # Input: nums = [1, 3, 5, 6], target = 7, Output: 4
    assert Solution.searchInsert([1, 3, 5, 6], 7) == 4


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

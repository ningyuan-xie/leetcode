"""35. Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy
Description: Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order."""

from typing import List


class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Loop through the index of the numbers in the list
        for i in range(len(nums)):
            # If the target is found, return the index
            if nums[i] == target:
                return i
            # If the target is less than the number at the index, return the index
            if nums[i] > target:
                return i
        # If the target is greater than all the numbers in the list, return the length of the list
        return len(nums)


# Unit Test: Input: nums = [1, 3, 5, 6], target = 5, Output: 2
assert Solution.searchInsert([1, 3, 5, 6], 5) == 2

# Unit Test: Input: nums = [1, 3, 5, 6], target = 2, Output: 1
assert Solution.searchInsert([1, 3, 5, 6], 2) == 1

# Unit Test: Input: nums = [1, 3, 5, 6], target = 7, Output: 4
assert Solution.searchInsert([1, 3, 5, 6], 7) == 4

print("All unit tests are passed")


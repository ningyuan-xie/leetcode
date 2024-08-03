"""283. Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy
Description: Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array."""

from typing import List


class Solution:
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the left and right pointers
        left, right = 0, 0
        # Move the right pointer to the end of the array
        while right < len(nums):  # E.g. [0, 1, 0, 3, 12]
            # If the right pointer is not zero, swap the left and right pointers' elements
            # left pointer is always at a zero element to be swapped
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # Move the left pointer to the next zero element to be swapped
            right += 1  # Move the right pointer to the next element to be checked
            # [0, 1, 0, 3, 12] -> [1, 0, 0, 3, 12] -> [1, 3, 0, 0, 12] -> [1, 3, 12, 0, 0]


# Unit Test: Input: nums = [0,1,0,3,12], Output: [1,3,12,0,0]
nums_test = [0, 1, 0, 3, 12]
Solution.moveZeroes(nums_test)
assert nums_test == [1, 3, 12, 0, 0]

# Unit Test: Input: nums = [0], Output: [0]
nums_test = [0]
Solution.moveZeroes(nums_test)
assert nums_test == [0]

# Unit Test: Input: nums = [0,0,0,0,0], Output: [0,0,0,0,0]
nums_test = [0, 0, 0, 0, 0]
Solution.moveZeroes(nums_test)
assert nums_test == [0, 0, 0, 0, 0]

# Unit Test: Input: nums = [1,0,2,3,4,5], Output: [1,2,3,4,5,0]
nums_test = [1, 0, 2, 3, 4, 5]
Solution.moveZeroes(nums_test)
assert nums_test == [1, 2, 3, 4, 5, 0]

print("All unit tests are passed")

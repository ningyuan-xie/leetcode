"""905. Sort Array By Parity
Link: https://leetcode.com/problems/sort-array-by-parity/
Difficulty: Easy
Description: Given an integer array nums, move all the even integers at the beginning of the array
followed by all the odd integers. Return any array that satisfies this condition."""

from typing import List


class Solution:
    @staticmethod
    def sortArrayByParity(nums: List[int]) -> List[int]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the two pointers
        left, right = 0, len(nums) - 1

        # Move the even integers to the left and the odd integers to the right
        while left < right:
            # If even, skip it, and +1 to disregard the ignored even integer
            if nums[left] % 2 == 0:
                left += 1
            # If odd, swap it with the right integer, and -1 to disregard the swapped odd integer
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        return nums


# Unit Test: Input: nums = [3,1,2,4], Output: [4,2,1,3]
assert Solution.sortArrayByParity([3, 1, 2, 4]) == [4, 2, 1, 3]

# Unit Test: Input: nums = [0], Output: [0]
assert Solution.sortArrayByParity([0]) == [0]

# Unit Test: Input: nums = [1], Output: [1]
assert Solution.sortArrayByParity([1]) == [1]

print("All unit tests are passed")

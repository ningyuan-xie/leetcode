# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Difficulty: Easy
# Description: Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

from typing import List


class Solution:
    # Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def findDisappearedNumbers(nums: List[int]) -> List[int]:
        # Iterate through the array
        for i in range(len(nums)):
            # Get the absolute value of the current number
            num = abs(nums[i])
            # Get the index of the number
            index = num - 1
            # If the number at the index is positive, make it negative
            if nums[index] > 0:
                nums[index] *= -1
        # Initialize the list of missing numbers
        missing_nums = []
        # Iterate through the array
        for i in range(len(nums)):
            # If the number at the index is positive, add the index + 1 to the missing numbers
            if nums[i] > 0:
                missing_nums.append(i + 1)
        return missing_nums


# Unit Test: Input: nums = [4, 3, 2, 7, 8, 2, 3, 1], Output: [5, 6]
assert Solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

# Unit Test: Input: nums = [1, 1], Output: [2]
assert Solution.findDisappearedNumbers([1, 1]) == [2]

# Unit Test: Input: nums = [1], Output: []
assert Solution.findDisappearedNumbers([1]) == []

print("All unit tests are passed")

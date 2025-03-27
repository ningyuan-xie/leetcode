"""1. Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Description: Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same
element twice.
You can return the answer in any order."""

from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """static method: does not require access to class or instance, so does not need self.
           instance method: needs access to class or instance, so needs self.
           Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Create dictionary with key-value pairs to store the number and index
        num_dict = {}

        # Loop through list and get the index and number
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - num
            # If the difference is already in the dictionary, we have found the twoSum number
            # so return the list index of the difference and the list index of the current number
            if diff in num_dict:
                return [num_dict[diff], i]
            # Otherwise, add the current number and list index to the dictionary for later use
            else:
                num_dict[num] = i

        return []


# Unit Test: Input: nums = [2,7,11,15], target = 9, Output: [0,1]
assert Solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

# Unit Test: Input: nums = [3,2,4], target = 6, Output: [1,2]
assert Solution.twoSum([3, 2, 4], 6) == [1, 2]

# Unit Test: Input: nums = [3,3], target = 6, Output: [0,1]
assert Solution.twoSum([3, 3], 6) == [0, 1]

print("All unit tests are passed")

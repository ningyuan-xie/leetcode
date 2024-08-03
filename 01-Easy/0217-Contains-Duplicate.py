"""217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Description: Given an integer array nums, return true if any value
appears at least twice in the array, and return false if every element is distinct."""

from typing import List


class Solution:
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        """Optimal Solution: Hash Set. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 0202-Happy-Number.py"""
        # Initialize a set to store the UNIQUE elements
        unique_set = set()
        # Iterate through the list
        for num in nums:
            # Check if the element is already in the set
            if num in unique_set:
                return True
            # Otherwise, add the element to the set
            unique_set.add(num)
        return False


# Unit Test: Input: nums = [1,2,3,1], Output: True
assert Solution.containsDuplicate([1, 2, 3, 1]) == True

# Unit Test: Input: nums = [1,2,3,4], Output: False
assert Solution.containsDuplicate([1, 2, 3, 4]) == False

# Unit Test: Input: nums = [1,1,1,3,3,4,3,2,4,2], Output: True
assert Solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

print("All unit tests are passed")

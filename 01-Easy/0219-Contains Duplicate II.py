"""219. Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/
Difficulty: Easy
Description: Given an integer array nums and an integer k, return true if there
are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k."""

from typing import List


class Solution:
    @staticmethod
    def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 0001-Two-Sum.py"""
        # Initialize a dictionary to store the element and its index
        num_dict = {}
        # Iterate through the list
        for i, num in enumerate(nums):
            # Check if the element is already in the dictionary
            # and the difference between the indices is less than or equal to k
            if num in num_dict and i - num_dict[num] <= k:
                return True
            # Update the index of the element in the dictionary
            num_dict[num] = i
        return False


# Unit Test: Input: nums = [1,2,3,1], k = 3, Output: True
assert Solution.containsNearbyDuplicate([1, 2, 3, 1], 3) == True

# Unit Test: Input: nums = [1,0,1,1], k = 1, Output: True
assert Solution.containsNearbyDuplicate([1, 0, 1, 1], 1) == True

# Unit Test: Input: nums = [1,2,3,1,2,3], k = 2, Output: False
assert Solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False

print("All unit tests are passed")

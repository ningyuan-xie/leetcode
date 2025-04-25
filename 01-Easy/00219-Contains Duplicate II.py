"""219. Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/
Difficulty: Easy
Description: Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k."""

from typing import List


class Solution:
    @staticmethod
    def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n).
        Similar to 1. Two Sum."""
        num_indices = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Check if the element is already in the dictionary
            if num in num_indices:
                # Check if the absolute difference of indices is less than or equal to k
                if i - num_indices[num] <= k:
                    return True
            # Update the last seen index of the element
            num_indices[num] = i
        return False


def unit_tests():
    # Input: nums = [1,2,3,1], k = 3, Output: True
    assert Solution.containsNearbyDuplicate([1, 2, 3, 1], 3) is True

    # Input: nums = [1,0,1,1], k = 1, Output: True
    assert Solution.containsNearbyDuplicate([1, 0, 1, 1], 1) is True

    # Input: nums = [1,2,3,1,2,3], k = 2, Output: False
    assert Solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

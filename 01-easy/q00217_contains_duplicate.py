"""217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

from typing import List


class Solution:
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)."""
        num_set = set()
        
        # Iterate through the list
        for num in nums:
            # Check if the element is already in the set
            if num in num_set:
                return True
            # Add the element to the set
            num_set.add(num)
        return False


def unit_tests():
    # Input: nums = [1,2,3,1], Output: True
    assert Solution.containsDuplicate([1, 2, 3, 1]) is True

    # Input: nums = [1,2,3,4], Output: False
    assert Solution.containsDuplicate([1, 2, 3, 4]) is False

    # Input: nums = [1,1,1,3,3,4,3,2,4,2], Output: True
    assert Solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

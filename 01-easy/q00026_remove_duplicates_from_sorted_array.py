"""26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
Description: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
• Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
• Return k."""

from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the new length index to 1
        length_new = 1
        # Loop through the list starting from the second element
        for i in range(1, len(nums)):
            # If the current number != previous number, keep it at the new length index
            if nums[i] != nums[i - 1]:
                # Replace the new length number in-place with the current number
                nums[length_new] = nums[i]
                # Increase the new length index
                length_new += 1
        # Return the length of the list, minimal length is 1
        return length_new


def unit_tests():
    # Input: nums = [1,1,2], Output: 2
    assert Solution.removeDuplicates([1, 1, 2]) == 2

    # Input: nums = [0,0,1,1,1,2,2,3,3,4], Output: 5
    assert Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5

    # Input: nums = [1,2,3], Output: 3
    assert Solution.removeDuplicates([1, 2, 3]) == 3


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

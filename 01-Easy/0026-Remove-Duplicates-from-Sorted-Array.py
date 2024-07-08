# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Description: Given a sorted array nums, remove the duplicates in-place
# such that each element appears only once and returns the new length.

from typing import List


class Solution:
    # Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        # Initialize unique numbers index to 0
        length_unique = 0  # pointer one
        # Loop begin from the second number
        for i in range(1, len(nums)):  # pointer two: index i
            # If the current number nums[i] != previous number nums[length_unique], unique number found
            if nums[i] != nums[length_unique]:
                # Increase the length of the unique numbers
                length_unique += 1
                # Replace nums[length_unique] with the unique number to compared with the next nums[i]
                nums[length_unique] = nums[i]
        # Return the length of the list with unique numbers, minimal length is 1
        return length_unique + 1


# Unit Test: Input: nums = [1,1,2], Output: 2
assert Solution.removeDuplicates([1, 1, 2]) == 2

# Unit Test: Input: nums = [0,0,1,1,1,2,2,3,3,4], Output: 5
assert Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5

# Unit Test: Input: nums = [1,2,3], Output: 3
assert Solution.removeDuplicates([1, 2, 3]) == 3

print("All unit tests are passed")

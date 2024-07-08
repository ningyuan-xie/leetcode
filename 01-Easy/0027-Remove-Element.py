# Link: https://leetcode.com/problems/remove-element/
# Difficulty: Easy
# Description: Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place and return the new length.

from typing import List


class Solution:
    # Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        # Initialize the new length index to 0
        length_new = 0  # pointer one
        # Loop through the list
        for i in range(len(nums)):  # pointer two: index i
            # If the current number != val, keep it at the new length index
            if nums[i] != val:  # E.g. val = 3, nums = [3, 2, 2, 3]
                # Replace the new length number in-place with the current number
                nums[length_new] = nums[i]
                # Increase the new length index
                length_new += 1
        # Return the length of the list, minimal length is 0
        return length_new


# Unit Test: Input: nums = [3,2,2,3], val = 3, Output: 2; nums = [2,2,_,_]
assert Solution.removeElement([3, 2, 2, 3], 3) == 2

# Unit Test: Input: nums = [0,1,2,2,3,0,4,2], val = 2, Output: 5; nums = [0,1,3,0,4,_]
assert Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5

# Unit Test: Input: nums = [1], val = 1, Output: 0; nums = []
assert Solution.removeElement([1], 1) == 0

print("All unit tests are passed")

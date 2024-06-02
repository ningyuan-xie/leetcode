# Link: https://leetcode.com/problems/remove-element/
# Difficulty: Easy
# Description: Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place and return the new length.

class Solution:
    @staticmethod
    def removeElement(nums: list[int], val: int) -> int:
        # Initialize the index to 0
        i = 0
        # Loop through the list
        for j in range(len(nums)):
            # If the current number is not equal to the value
            if nums[j] != val:
                # Update the current number to the next number
                nums[i] = nums[j]
                # Increment the index
                i += 1
        # Return the length of the list
        return i


# Unit Test: Input: nums = [3,2,2,3], val = 3, Output: 2
assert Solution.removeElement([3, 2, 2, 3], 3) == 2

# Unit Test: Input: nums = [0,1,2,2,3,0,4,2], val = 2, Output: 5
assert Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5

# Unit Test: Input: nums = [1], val = 1, Output: 0
assert Solution.removeElement([1], 1) == 0
print("All unit tests are passed")

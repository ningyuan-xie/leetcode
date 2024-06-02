# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Description: Given a sorted array nums, remove the duplicates in-place
# such that each element appears only once and returns the new length.

class Solution:
    @staticmethod
    def removeDuplicates(nums: list[int]) -> int:
        # Initialize the index to 0
        i = 0
        # Loop through the list
        for j in range(1, len(nums)):
            # If the current number is not equal to the previous number
            if nums[j] != nums[i]:
                # Increment the index
                i += 1
                # Update the current number to the next number
                nums[i] = nums[j]
        # Return the length of the list
        return i + 1


# Unit Test: Input: nums = [1,1,2], Output: 2
assert Solution.removeDuplicates([1, 1, 2]) == 2

# Unit Test: Input: nums = [0,0,1,1,1,2,2,3,3,4], Output: 5
assert Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5

# Unit Test: Input: nums = [1,2,3], Output: 3
assert Solution.removeDuplicates([1, 2, 3]) == 3
print("All unit tests are passed")

"""977. Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Difficulty: Easy
Description: Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order."""

from typing import List


class Solution:
    @staticmethod
    def sortedSquares(nums: List[int]) -> List[int]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the result array
        result = [0] * len(nums)

        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1

        # Loop through the result array in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # If the absolute value of the left pointer is greater than the right pointer
            if abs(nums[left]) > abs(nums[right]):
                # Set the result array to the square of the left pointer
                result[i] = nums[left] * nums[left]
                # Move the left pointer to the right
                left += 1
            # Otherwise
            else:
                # Set the result array to the square of the right pointer
                result[i] = nums[right] * nums[right]
                # Move the right pointer to the left
                right -= 1

        # Return the result array
        return result


# Unit Test: Input: [-4,-1,0,3,10], Output: [0,1,9,16,100]
assert Solution.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

# Unit Test: Input: [-7,-3,2,3,11], Output: [4,9,9,49,121]
assert Solution.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

print("All unit tests are passed")

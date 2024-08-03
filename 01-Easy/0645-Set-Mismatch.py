"""645. Set Mismatch
Link: https://leetcode.com/problems/set-mismatch/
Difficulty: Easy
Description: You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in
the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and
return them in the form of an array."""

from typing import List


class Solution:
    @staticmethod
    def findErrorNums(nums: List[int]) -> List[int]:
        """Optimal Solution: Mark the visited number. Time Complexity: O(n), Space Complexity: O(1)
           Similar to 0448-Find-All-Numbers-Disappeared-in-an-Array.py"""
        # Initialize the duplicate and missing numbers
        duplicate, missing = 0, 0

        # Traverse all the numbers in the array to find the duplicate number first
        for num in nums:
            # Starts with the positive number
            num = abs(num)
            # If the number is already visited, then it is the duplicate number
            if nums[num - 1] < 0:  # num - 1 because 0-based index and nums should start from 1
                duplicate = num
            # Mark the number as visited
            else:
                nums[num - 1] *= -1  # num - 1 because 0-based index and nums should start from 1

        # Now that all the visited numbers are negative, the remaining positive is the missing number
        for i, num in enumerate(nums):
            if num > 0:
                # Get missing number from index
                missing = i + 1
                break
        return [duplicate, missing]


# Unit Test: Input: nums = [1, 2, 2, 4], Output: [2, 3]
assert Solution.findErrorNums([1, 2, 2, 4]) == [2, 3]

# Unit Test: Input: nums = [1, 1], Output: [1, 2]
assert Solution.findErrorNums([1, 1]) == [1, 2]

# Unit Test: Input: nums = [2, 2], Output: [2, 1]
assert Solution.findErrorNums([2, 2]) == [2, 1]

print("All unit tests are passed")

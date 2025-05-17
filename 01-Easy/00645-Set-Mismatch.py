"""645. Set Mismatch
Link: https://leetcode.com/problems/set-mismatch/
Difficulty: Easy
Description: You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array."""

from typing import List


class Solution:
    @staticmethod
    def findErrorNums(nums: List[int]) -> List[int]:
        """Optimal Solution: Cyclic Sort. Time Complexity: O(n), Space Complexity: O(1).
        Similar to 448. Find All Numbers Disappeared in an Array."""
        # Initialize the duplicate and missing numbers
        duplicate, missing = 0, 0
        
        # Cyclic sort to find the duplicate
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                # Swap the elements until nums[i] is at its rightful home
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        
        # After sorting, find the first number not in its correct position
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicate = nums[i]
                missing = i + 1
                break
                
        return [duplicate, missing]


def unit_tests():
    # Input: nums = [1, 2, 2, 4], Output: [2, 3]
    assert Solution.findErrorNums([1, 2, 2, 4]) == [2, 3]

    # Input: nums = [1, 1], Output: [1, 2]
    assert Solution.findErrorNums([1, 1]) == [1, 2]

    # Input: nums = [2, 2], Output: [2, 1]
    assert Solution.findErrorNums([2, 2]) == [2, 1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

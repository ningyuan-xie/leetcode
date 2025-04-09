"""448. Find All Numbers Disappeared in an Array
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Difficulty: Easy
Description: Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
Follow up: Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space."""

from typing import List


class Solution:
    @staticmethod
    def findDisappearedNumbers(nums: List[int]) -> List[int]:
        """Optimal Solution: Mark the visited number. Time Complexity: O(n), Space Complexity: O(1).
           The trick is to utilize the input array itself for marking the presence of numbers.
           Logic: input number -> -1 becomes index -> +1 becomes output number"""
        # The 1st loop marks index's number as negative to denote the presence of each number
        for num in nums:  # E.g. [1, 2, 2, 4], missing numbers: [3]
            # Starts with the positive number
            num = abs(num)
            # Mark the number as visited using negation without using extra space
            if nums[num - 1] > 0:
                nums[num - 1] *= -1  # [-1, -2, 2, -4], index 2 is the duplicate and the missing number

        # The 2nd loop identifies the index's number that remain positive, indicating the missing index
        missing_nums = []
        for i, num in enumerate(nums):
            if num > 0:
                # Get missing number from index
                missing_nums.append(i + 1)
        return missing_nums

    @staticmethod
    def findDisappearedNumbersSet(nums: List[int]) -> List[int]:
        """Alternative Solution: Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the set of numbers
        nums_set = set(nums)
        # Initialize the list of missing numbers
        missing_nums = []
        # Iterate through the range of 1 to the length of the array
        for i in range(1, len(nums) + 1):
            # If the number is not in the set, add it to the missing numbers
            if i not in nums_set:
                missing_nums.append(i)
        return missing_nums


# Input: nums = [4, 3, 2, 7, 8, 2, 3, 1], Output: [5, 6]
assert Solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

# Input: nums = [1, 1], Output: [2]
assert Solution.findDisappearedNumbersSet([1, 1]) == [2]

# Input: nums = [1], Output: []
assert Solution.findDisappearedNumbersSet([1]) == []

print("All unit tests are passed.")

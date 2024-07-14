# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Difficulty: Easy
# Description: Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.
# Follow up: Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.

from typing import List


class Solution:
    # Optimal Solution: Negation. Time Complexity: O(n), Space Complexity: O(1)
    # The trick is to utilize the input array itself for marking the presence of numbers
    # Logic: input number -> -1 becomes index -> +1 becomes output number
    @staticmethod
    def findDisappearedNumbers(nums: List[int]) -> List[int]:
        # The 1st loop marks index's number as negative to denote the presence of each number
        for num in nums:  # E.g. [4, 3, 2, 7, 8, 2, 3, 1], missing numbers: [5, 6]
            # Get the 0-based index of the number
            index = abs(num) - 1  # 3, 2, 1, 6, 7, 1, 2, 0
            # Using negation allows us to mark the presence of a number without using extra space
            nums[index] = -abs(nums[index])  # [-4, -3, -2, -7, -8, 2, 3, -1]

        # The 2nd loop identifies the index's number that remain positive, indicating the missing index
        missing_nums = []
        for i, num in enumerate(nums):
            if num > 0:
                missing_nums.append(i + 1)
        return missing_nums

    # Alternative Solution: Set. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def findDisappearedNumbersSet(nums: List[int]) -> List[int]:
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


# Unit Test: Input: nums = [4, 3, 2, 7, 8, 2, 3, 1], Output: [5, 6]
assert Solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

# Unit Test: Input: nums = [1, 1], Output: [2]
assert Solution.findDisappearedNumbersSet([1, 1]) == [2]

# Unit Test: Input: nums = [1], Output: []
assert Solution.findDisappearedNumbersSet([1]) == []

print("All unit tests are passed")

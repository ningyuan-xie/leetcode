"""2553. Separate the Digits in an Array
Link: https://leetcode.com/problems/separate-the-digits-in-an-array/
Difficulty: Easy
Description: Given an array of positive integers nums, return an array answer that consists of the
digits of each integer in nums after separating them in the same order they appear in nums.
To separate the digits of an integer is to get all the digits it has in the same order.
For example, for the integer 10921, the separation of its digits is [1,0,9,2,1]."""

from typing import List


class Solution:
    @staticmethod
    def separateDigits(nums: List[int]) -> List[int]:
        """Optimal Solution: List Comprehension. Time Complexity: O(n), Space Complexity: O(n)"""
        return [int(digit) for num in nums for digit in str(num)]


# Unit Test: nums = [13,25,83,77], Output: [1,3,2,5,8,3,7,7]
assert Solution.separateDigits([13, 25, 83, 77]) == [1, 3, 2, 5, 8, 3, 7, 7]

# Unit Test: nums = [7,1,3,9], Output: [7,1,3,9]
assert Solution.separateDigits([7, 1, 3, 9]) == [7, 1, 3, 9]

print("All unit tests are passed")

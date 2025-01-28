"""2535. Difference Between Element Sum and Digit Sum of an Array
Link: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
Difficulty: Easy
Description: You are given a positive integer array nums.
- The element sum is the sum of all the elements in nums.
- The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.
Note that the absolute difference between two integers x and y is defined as |x - y|."""

from typing import List


class Solution:
    @staticmethod
    def differenceOfSum(nums: List[int]) -> int:
        """Optimal Solution: Int and String Conversion. Time Complexity: O(n), Space Complexity: O(1)"""
        element_sum = 0
        digit_sum = 0

        for num in nums:  # E.g. nums = [1, 15, 6, 3]
            element_sum += num  # 1 + 15 + 6 + 3 = 25
            digit_sum += sum(int(digit) for digit in str(num))  # 1 + 1 + 5 + 6 + 3 = 16

        return abs(element_sum - digit_sum)


# Unit Test: nums = [1,15,6,3], Output: 9
assert Solution.differenceOfSum([1, 15, 6, 3]) == 9

# Unit Test: nums = [1,2,3,4], Output: 0
assert Solution.differenceOfSum([1, 2, 3, 4]) == 0

print("All unit tests are passed")



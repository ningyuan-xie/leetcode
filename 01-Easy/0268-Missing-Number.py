# Link: https://leetcode.com/problems/missing-number/
# Difficulty: Easy
# Description: Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

from typing import List


class Solution:
    # Optimal Solution: Bit Manipulation. Time Complexity: O(n), Space Complexity: O(1)
    # Similar to the XOR operation in 0136-Single-Number.py
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        # Initialize the missing number as the length of the array because:
        # 1. Ensure that the highest possible number (could be the missing one) is included in the XOR
        # 2. Index i won't reach the max number, requiring the length to cancel out the max number
        missing_number = len(nums)
        # XOR operation will cancel out all the numbers that appear both
        # as indices and values in the array, leaving only the missing number
        for i, num in enumerate(nums):
            missing_number ^= i ^ num
            # 3 ^ (0 ^ 3) ^ (1 ^ 0) ^ (2 ^ 1) = 2
            # Ideally if no missing number: (0 ^ 3) ^ (1 ^ 0) ^ (2 ^ 1) ^ (3 ^ 2) = 0
        return missing_number

    # Optimal Solution: Gauss's Formula. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def missingNumberSumFormula(nums: List[int]) -> int:
        # Calculate the sum of the numbers from 0 to n using the formula: sum = n * (n + 1) / 2
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        # Calculate the actual sum of the numbers in the array
        actual_sum = sum(nums)
        # The difference between the expected and actual sum is the missing number
        return expected_sum - actual_sum


# Unit Test: Input: nums = [3,0,1], n = 3 since there are 3 numbers,
# so all numbers are in range [0, 3]. 2 is the missing number.
assert Solution.missingNumber([3, 0, 1]) == 2

# Unit Test: Input: nums = [0,1], n = 2 since there are 2 numbers,
# so all numbers are in range [0, 2]. 2 is the missing number.
assert Solution.missingNumberSumFormula([0, 1]) == 2  # 2 ^ (0 ^ 2) ^ (1 ^ 0) = 2

# Unit Test: Input: nums = [9,6,4,2,3,5,7,0,1], n = 9 since there are 9 numbers,
# so all numbers are in range [0, 9]. 8 is the missing number.
assert Solution.missingNumberSumFormula([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

print("All unit tests are passed")

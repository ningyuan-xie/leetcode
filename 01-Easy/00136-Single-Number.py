"""136. Single Number
Link: https://leetcode.com/problems/single-number/
Difficulty: Easy
Description: Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space."""

from typing import List


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(n), Space Complexity: O(1).
           Bitwise XOR operator ^ : 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0."""
        result = 0  # nums ^ 0 = nums
        for num in nums:  # E.g. nums = [4, 1, 2, 1, 2]
            # XOR operation: result = result XOR num
            result ^= num
            # result = 0 (0000) XOR 4 (0100) = 4 (0100),
            # result = 4 (0100) XOR 1 (0001) = 5 (0101),
            # result = 5 (0101) XOR 2 (0010) = 7 (0111),
            # result = 7 (0111) XOR 1 (0001) = 6 (0110),
            # result = 6 (0110) XOR 2 (0010) = 4 (0100)
        return result


# Unit Test: Input: nums = [2,2,1], Output: 1
assert Solution.singleNumber([2, 2, 1]) == 1

# Unit Test: Input: nums = [4,1,2,1,2], Output: 4
assert Solution.singleNumber([4, 1, 2, 1, 2]) == 4

# Unit Test: Input: nums = [1], Output: 1
assert Solution.singleNumber([1]) == 1

print("All unit tests are passed")

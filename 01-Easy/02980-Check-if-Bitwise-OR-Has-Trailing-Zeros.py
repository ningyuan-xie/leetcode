"""2980. Check if Bitwise OR Has Trailing Zeros
Link: https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros
Difficulty: Easy
Description: You are given an array of positive integers nums.
You have to check if it is possible to select two or more elements in the array such that the
bitwise OR of the selected elements has at least one trailing zero in its binary representation.
For example, the binary representation of 5, which is "101", does not have any trailing zeros,
whereas the binary representation of 4, which is "100", has two trailing zeros.
Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros,
return false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def hasTrailingZeros(nums: List[int]) -> bool:
        """Optimal Solution: Check if array contains more than 1 even number.
           Time Complexity: O(n), Space Complexity: O(1).
           Bitwise XOR operator ^ : 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0"""
        count = 0
        for num in nums:
            if num % 2 == 0:
                count += 1
            if count > 1:
                return True
        return False


# Unit Test: nums = [1,2,3,4,5], Output: True
assert Solution.hasTrailingZeros([1, 2, 3, 4, 5]) is True

# Unit Test: nums = [2,4,8,16], Output: True
assert Solution.hasTrailingZeros([2, 4, 8, 16]) is True

# Unit Test: nums = [1,3,5,7,9], Output: False
assert Solution.hasTrailingZeros([1, 3, 5, 7, 9]) is False

print("All unit tests are passed")

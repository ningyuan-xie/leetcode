"""3190. Find Minimum Operations to Make All Elements Divisible by Three
Link: https://leetcode.com/problems/Find-Minimum-Operations-to-Make-All-Elements-Divisible-by-Three
Difficulty: Easy
Description: You are given an integer array nums. In one operation, you can add or subtract 1
from any element of nums.
Return the minimum number of operations to make all elements of nums divisible by 3."""

from typing import List


class Solution:
    @staticmethod
    def minimumOperations(nums: List[int]) -> int:
        """Optimal Solution: Counting. Time Complexity: O(n), Space Complexity: O(1)
           Count 1 every time if not divisible by 3"""
        return sum(num % 3 != 0 for num in nums)


# Unit Test: nums = [1,2,3,4], Output = 3
assert Solution.minimumOperations([1, 2, 3, 4]) == 3

# Unit Test: nums = [3,6,9], Output = 0
assert Solution.minimumOperations([3, 6, 9]) == 0

print("All unit tests are passed")

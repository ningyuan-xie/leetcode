"""2154. Keep Multiplying Found Values by Two
Link: https://www.leetcode.com/problems/keep-multiplying-found-values-by-two
Difficulty: Easy
Description: You are given an array of integers nums. You are also given an integer original
which is the first number that needs to be searched for in nums.
You then do the following steps:
1. If original is found in nums, multiply it by two (i.e., set original = 2 * original).
2. Otherwise, stop the process.
3. Repeat this process with the new number as long as you keep finding the number.
Return the final value of original."""

from typing import List


class Solution:
    @staticmethod
    def findFinalValue(nums: List[int], original: int) -> int:
        """Optimal Solution: While Loop. Time Complexity: O(n), Space Complexity: O(1)"""
        while original in nums:
            original *= 2
        return original


# Unit Test: nums = [5,3,6,1,12], original = 3, Output: 24
assert Solution.findFinalValue([5, 3, 6, 1, 12], 3) == 24

# Unit Test: nums = [2,7,9], original = 4, Output: 4
assert Solution.findFinalValue([2, 7, 9], 4) == 4

print("All unit tests are passed.")

"""1929. Concatenation of Array
Link: https://leetcode.com/problems/concatenation-of-array/
Difficulty: Easy
Description: Given an integer array nums of length n, you want to create an array ans of length
2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans."""

from typing import List


class Solution:
    @staticmethod
    def getConcatenation(nums: List[int]) -> List[int]:
        """Optimal Solution: Double the Array. Time Complexity: O(n), Space Complexity: O(n)"""
        return nums + nums


# Unit Test: nums = [1, 2, 1], Output: [1, 2, 1, 1, 2, 1]
assert Solution.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]

# Unit Test: nums = [1, 3, 2, 1], Output: [1, 3, 2, 1, 1, 3, 2, 1]
assert Solution.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]

# Unit Test: nums = [1, 2, 3, 4], Output: [1, 2, 3, 4, 1, 2, 3, 4]
assert Solution.getConcatenation([1, 2, 3, 4]) == [1, 2, 3, 4, 1, 2, 3, 4]

print("All unit tests are passed")

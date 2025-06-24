"""2529. Maximum Count of Positive Integer and Negative Integer
Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
Difficulty: Easy
Description: Given an array nums sorted in non-decreasing order, return the maximum between the number
of positive integers and the number of negative integers.
In other words, if the number of positive integers in nums is pos and the number of negative integers
is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative."""

from typing import List


class Solution:
    @staticmethod
    def maxCount(nums: List[int]) -> int:
        """Optimal Solution: Count Positive and Negative Integers.
           Time Complexity: O(n), Space Complexity: O(1)."""
        pos, neg = 0, 0

        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1

        return max(pos, neg)


# Input: nums = [-2,-1,-1,1,2,3], Output: 3
assert Solution.maxCount([-2, -1, -1, 1, 2, 3]) == 3

# Input: nums = [-3,-2,-1,0,0,1,2], Output: 3
assert Solution.maxCount([-3, -2, -1, 0, 0, 1, 2]) == 3

# Input: nums = [5,20,66,1314], Output: 4
assert Solution.maxCount([5, 20, 66, 1314]) == 4

print("All unit tests are passed.")

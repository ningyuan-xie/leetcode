"""2788. Sum of Squares of Special Elements
Link: https://leetcode.com/problems/sum-of-squares-of-special-elements/
Difficulty: Easy
Description: You are given a 1-indexed integer array nums of length n.
An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
Return the sum of the squares of all special elements of nums."""

from typing import List


class Solution:
    @staticmethod
    def sumOfSquares(nums: List[int]) -> int:
        """Optimal Solution: Math. Time Complexity: O(n), Space Complexity: O(1)"""
        # enumerate(nums, 1) to start the index from 1
        return sum(num * num
                   for (index, num) in enumerate(nums, 1)
                   if len(nums) % index == 0)


# Unit Test: nums = [1,2,3,4], Output: 21
assert Solution.sumOfSquares([1, 2, 3, 4]) == 21

# Unit Test: nums = [2,7,1,19,18,3], Output: 63
assert Solution.sumOfSquares([2, 7, 1, 19, 18, 3]) == 63

print("All unit tests are passed.")

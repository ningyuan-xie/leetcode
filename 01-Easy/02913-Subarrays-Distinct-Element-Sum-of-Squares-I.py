"""2913. Subarrays with Distinct Elements and Sum of Squares I
Link: https://leetcode.com/problems/subarrays-with-distinct-elements-and-sum-of-squares-i/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums.
The distinct count of a subarray of nums is defined as:
- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that
0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct
count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.
A subarray is a contiguous non-empty sequence of elements within an array."""

from typing import List


class Solution:
    @staticmethod
    def sumCounts(nums: List[int]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n^2), Space Complexity: O(n)"""
        n = len(nums)
        ans = 0

        distinct = set()
        # Each outer loop, reset the distinct set for the new subarray
        for i in range(n):
            for j in range(i, n):
                distinct.add(nums[j])
                ans += len(distinct) ** 2
            # Clear the set for the next iteration
            distinct.clear()

        return ans


# Unit Test: nums = [1,2,1], Output: 15
assert Solution.sumCounts([1, 2, 1]) == 15

# Unit Test: nums = [1,1], Output: 3
assert Solution.sumCounts([1, 1]) == 3

print("All unit tests are passed.")

"""2164. Sort Even and Odd Indices Independently
Link: https://www.leetcode.com/problems/sort-even-and-odd-indices-independently
Difficulty: Easy
Description: You are given a 0-indexed integer array nums. Rearrange the values of
nums according to the following rules:
1. Sort the values at odd indices of nums in non-increasing order.
- For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after.
The values at odd indices 1 and 3 are sorted in non-increasing order.
2. Sort the values at even indices of nums in non-decreasing order.
- For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after.
The values at even indices 0 and 2 are sorted in non-decreasing order.
Return the array formed after rearranging the values of nums."""

from typing import List


class Solution:
    @staticmethod
    def sortEvenOdd(nums: List[int]) -> List[int]:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(n)"""
        # Sort even-indexed elements (ascending)
        even = sorted(nums[::2])  # [4,1,2,3] -> [4,2] -> [2,4]
        # Sort odd-indexed elements (descending)
        odd = sorted(nums[1::2], reverse=True)  # [4,1,2,3] -> [1,3] -> [3,1]
        # Reassign sorted elements back to nums
        nums[::2], nums[1::2] = even, odd
        return nums


# Unit Test: nums = [4,1,2,3], Output: [2,3,4,1]
assert Solution.sortEvenOdd([4, 1, 2, 3]) == [2, 3, 4, 1]

# Unit Test: nums = [2,1], Output: [2,1]
assert Solution.sortEvenOdd([2, 1]) == [2, 1]

print("All unit tests are passed")

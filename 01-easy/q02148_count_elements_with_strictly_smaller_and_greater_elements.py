"""2148. Count Elements With Strictly Smaller and Greater Elements
Link: https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/
Difficulty: Easy
Description: Given an integer array nums, return the number of elements that have both a strictly
smaller and a strictly greater element appear in nums."""

from typing import List


class Solution:
    @staticmethod
    def countElements(nums: List[int]) -> int:
        """Optimal Solution: Sorting. Time Complexity: O(nlogn), Space Complexity: O(1)."""
        nums.sort()  # [11,7,2,15] -> [2,7,11,15]
        n = len(nums)
        count = 0

        for i in range(1, n - 1):
            if nums[0] < nums[i] < nums[-1]:
                count += 1
        return count


# Unit Test: nums = [11,7,2,15], Output: 2
assert Solution.countElements([11, 7, 2, 15]) == 2

# Unit Test: nums = [-3,3,3,90], Output: 2
assert Solution.countElements([-3, 3, 3, 90]) == 2

print("All unit tests are passed.")

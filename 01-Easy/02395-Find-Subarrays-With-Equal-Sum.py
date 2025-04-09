"""2395. Find Subarrays With Equal Sum
Link: https://leetcode.com/problems/find-subarrays-with-equal-sum/
Difficulty: Easy
Description: Given a 0-indexed integer array nums, determine whether there exist two subarrays of
length 2 with equal sum. Note that the two subarrays must begin at different indices.
Return true if these subarrays exist, and false otherwise.
A subarray is a contiguous non-empty sequence of elements within an array."""

from typing import List


class Solution:
    @staticmethod
    def findSubarrays(nums: List[int]) -> bool:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)"""
        seen = set()
        # Iterate through the array and check if the sum of two consecutive elements is already seen
        for i in range(len(nums) - 1):
            subarray_sum = nums[i] + nums[i + 1]
            if subarray_sum in seen:
                return True
            seen.add(subarray_sum)
        return False


# Unit Test: nums = [4,2,4], Output: true
assert Solution.findSubarrays([4, 2, 4]) is True

# Unit Test: nums = [1,2,3,4,5], Output: false
assert Solution.findSubarrays([1, 2, 3, 4, 5]) is False

# Unit Test: nums = [0,0,0], Output: true
assert Solution.findSubarrays([0, 0, 0]) is True

print("All unit tests are passed.")

"""2190. Most Frequent Number Following Key In an Array
Link: https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums. You are also given an integer key, which
is present in nums.
For every unique integer target in nums, count the number of times target immediately follows an
occurrence of key in nums. In other words, count the number of indices i such that:
- 0 <= i <= nums.length - 2,
- nums[i] == key and,
- nums[i + 1] == target.
Return the target with the maximum count. The test cases will be generated such that the target with
maximum count is unique."""

from typing import List


class Solution:
    @staticmethod
    def mostFrequent(nums: List[int], key: int) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Count occurrences of targets following the key
        target_count = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                target_count[nums[i + 1]] = target_count.get(nums[i + 1], 0) + 1
        # nums = [1,100,200,1,100], key = 1 -> target_count = {100: 2}
        # nums = [2,2,2,2,3], key = 2 -> target_count = {2: 3, 3: 1}

        # Find and return the most frequent target: finds the target with the
        # maximum count, breaking ties by choosing the smallest number
        return max(target_count, key=lambda x: (target_count[x], -x))


# Unit Test: nums = [1,100,200,1,100], key = 1, Output: 100
assert Solution.mostFrequent([1, 100, 200, 1, 100], 1) == 100

# Unit Test: nums = [2,2,2,2,3], key = 2, Output: 2
assert Solution.mostFrequent([2, 2, 2, 2, 3], 2) == 2

print("All unit tests are passed.")

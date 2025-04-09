"""594. Longest Harmonious Subsequence
Link: https://leetcode.com/problems/longest-harmonious-subsequence/
Difficulty: Easy
Description: We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all
its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no
elements without changing the order of the remaining elements."""

from typing import List


class Solution:
    @staticmethod
    def findLHS(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize a dictionary to store the frequency of each number
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        # Initialize the longest harmonious subsequence length
        longest_harmonious_subsequence = 0
        # Iterate over each number in the dictionary
        for num in num_freq:
            # Check if the current number + 1 exists in the dictionary
            if num + 1 in num_freq:
                # Update the longest harmonious subsequence length
                longest_harmonious_subsequence = max(longest_harmonious_subsequence,
                                                     num_freq[num] + num_freq[num + 1])
        return longest_harmonious_subsequence


# Input: nums = [1, 3, 2, 2, 5, 2, 3, 7], Output: 5
assert Solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5

# Input: nums = [1, 2, 3, 4], Output: 2
assert Solution.findLHS([1, 2, 3, 4]) == 2

# Input: nums = [1, 1, 1, 1], Output: 0
assert Solution.findLHS([1, 1, 1, 1]) == 0

print("All unit tests are passed.")

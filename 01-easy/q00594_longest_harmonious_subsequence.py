"""594. Longest Harmonious Subsequence
Link: https://leetcode.com/problems/longest-harmonious-subsequence/
Difficulty: Easy
Description: We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences."""

from typing import List


class Solution:
    @staticmethod
    def findLHS(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        max_length = 0
        for num in freq:
            # Check if the current number + 1 exists in the dictionary
            if num + 1 in freq:
                # Update the longest harmonious subsequence length
                max_length = max(max_length, freq[num] + freq[num + 1])
                
        return max_length


def unit_tests():
    # Input: nums = [1, 3, 2, 2, 5, 2, 3, 7], Output: 5
    assert Solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5

    # Input: nums = [1, 2, 3, 4], Output: 2
    assert Solution.findLHS([1, 2, 3, 4]) == 2

    # Input: nums = [1, 1, 1, 1], Output: 0
    assert Solution.findLHS([1, 1, 1, 1]) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

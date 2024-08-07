"""697. Degree of an Array
Link: https://leetcode.com/problems/degree-of-an-array/
Difficulty: Easy
Description: Given a non-empty array of non-negative integers nums, the degree of this array is
defined as the maximum frequency of any one of its elements. Your task is to find the smallest
possible length of a (contiguous) subarray of nums, that has the same degree as nums."""

from typing import List


class Solution:
    @staticmethod
    def findShortestSubArray(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the hash table
        freq, first, last = {}, {}, {}

        # Iterate through the list of numbers and update the three hash tables
        for i, num in enumerate(nums):  # E.g. nums = [1, 2, 2, 3, 1]
            # Update the frequency of the number
            freq[num] = freq.get(num, 0) + 1  # freq: {1: 2, 2: 2, 3: 1}
            # Update the first appearance of each number using .setdefault()
            first.setdefault(num, i)  # first: {1: 0, 2: 1, 3: 3}
            # Update the last appearance of each number
            last[num] = i  # last: {1: 4, 2: 2, 3: 3}

        # Find the maximum frequency of any one of the elements as the degree
        degree = max(freq.values())  # max_freq = 2

        # Find the smallest possible length of the subarray
        # last[1] - first[1] + 1 = 5; last[2] - first[2] + 1 = 2 -> the smallest subarray is [2, 2]
        return min(last[num] - first[num] + 1 for num in freq if freq[num] == degree)


# Unit Test: Input: nums = [1, 2, 2, 3, 1], Output: 2
assert Solution.findShortestSubArray([1, 2, 2, 3, 1]) == 2

# Unit Test: Input: nums = [1, 2, 2, 3, 1, 4, 2], Output: 6
assert Solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6

print("All unit tests are passed")

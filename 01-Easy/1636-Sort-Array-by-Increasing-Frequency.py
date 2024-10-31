"""1636. Sort Array by Increasing Frequency
Link: https://leetcode.com/problems/sort-array-by-increasing-frequency/
Difficulty: Easy
Description: Given an array of integers nums, sort the array in increasing order based on the
frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array."""

from typing import List


class Solution:
    @staticmethod
    def frequencySort(nums: List[int]) -> List[int]:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize frequency dictionary
        count = {}

        # Count the frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Sort by frequency first, then by value in decreasing order for ties
        nums.sort(key=lambda x: (count[x], -x))  # (count[x], -x) represents (frequency, value)

        return nums


# Unit Test: nums = [1, 1, 2, 2, 2, 3], Output: [3, 1, 1, 2, 2, 2]
assert Solution.frequencySort([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]

# Unit Test: nums = [2, 3, 1, 3, 2], Output: [1, 3, 3, 2, 2]
assert Solution.frequencySort([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]

# Unit Test: nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1], Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]
assert Solution.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1]

print("All unit tests are passed")

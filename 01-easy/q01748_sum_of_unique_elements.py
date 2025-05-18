"""1748. Sum of Unique Elements
Link: https://leetcode.com/problems/sum-of-unique-elements/
Difficulty: Easy
Description: You are given an integer array nums. The unique elements of an array are the elements
that appear exactly once in the array.
Return the sum of all the unique elements of nums."""

from typing import List


class Solution:
    @staticmethod
    def sum_of_unique(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the frequency of each element in the array
        freq = {}

        # Count the frequency of each element in the array
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sum the unique elements in the array
        return sum(num for (num, count) in freq.items() if count == 1)


# Unit Test: nums = [1, 2, 3, 2], Output: 4
assert Solution.sum_of_unique([1, 2, 3, 2]) == 4

# Unit Test: nums = [1, 1, 1, 1, 1], Output: 0
assert Solution.sum_of_unique([1, 1, 1, 1, 1]) == 0

# Unit Test: nums = [1, 2, 3, 4, 5], Output: 15
assert Solution.sum_of_unique([1, 2, 3, 4, 5]) == 15

print("All unit tests are passed.")

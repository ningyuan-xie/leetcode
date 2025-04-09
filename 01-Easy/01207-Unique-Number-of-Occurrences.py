"""1207. Unique Number of Occurrences
Link: https://leetcode.com/problems/unique-number-of-occurrences/
Difficulty: Easy
Description: Given an array of integers arr, write a function that returns true if and only if the
number of occurrences of each value in the array is unique."""

from typing import List


class Solution:
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        """Optimal Solution: Hash Table & Set.
           Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the frequency of each integer in arr
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Check if the number of occurrences of each value in arr is unique
        # freq.values(): dict_values([3, 2, 1])
        return len(freq) == len(set(freq.values()))


# Unit Test: arr = [1, 2, 2, 1, 1, 3], Output: True
assert Solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True

# Unit Test: arr = [1, 2], Output: False
assert Solution.uniqueOccurrences([1, 2]) is False

# Unit Test: arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], Output: True
assert Solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True

print("All unit tests are passed")


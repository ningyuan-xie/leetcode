"""1207. Unique Number of Occurrences
Link: https://leetcode.com/problems/unique-number-of-occurrences/
Difficulty: Easy
Description: Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        """Optimal Solution: Hash Table & Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the frequency of each integer in arr
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Check if the number of occurrences of each value in arr is unique
        return len(freq) == len(set(freq.values()))


def unit_tests():
    # Input: arr = [1, 2, 2, 1, 1, 3], Output: True
    assert Solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True

    # Input: arr = [1, 2], Output: False
    assert Solution.uniqueOccurrences([1, 2]) is False

    # Input: arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], Output: True
    assert Solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True


if __name__ == "__main__":  
    unit_tests()
    print("All unit tests are passed.")

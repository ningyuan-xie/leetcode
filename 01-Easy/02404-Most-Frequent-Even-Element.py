"""2404. Most Frequent Even Element
Link: https://leetcode.com/problems/most-frequent-even-element/
Difficulty: Easy
Description: Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1."""

from typing import List


class Solution:
    @staticmethod
    def mostFrequentEven(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Dictionary to store the frequency of each even element
        frequency = {}
        for num in nums:
            if num % 2 == 0:
                frequency[num] = frequency.get(num, 0) + 1

        # Find the most frequent even element
        most_frequent_even, max_frequency = -1, 0
        for num, freq in frequency.items():
            if freq > max_frequency or (freq == max_frequency and num < most_frequent_even):
                most_frequent_even, max_frequency = num, freq

        return most_frequent_even


# Unit Test: nums = [0,1,2,2,4,4,1], Output: 2
assert Solution.mostFrequentEven([0, 1, 2, 2, 4, 4, 1]) == 2

# Unit Test: nums = [4,4,4,9,2,4], Output: 4
assert Solution.mostFrequentEven([4, 4, 4, 9, 2, 4]) == 4

# Unit Test: nums = [29,47,21,41,13,37,25,7], Output: -1
assert Solution.mostFrequentEven([29, 47, 21, 41, 13, 37, 25, 7]) == -1

print("All unit tests are passed.")

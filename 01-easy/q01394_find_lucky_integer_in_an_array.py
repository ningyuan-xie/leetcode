"""1394. Find Lucky Integer in an Array
Link: https://leetcode.com/problems/find-lucky-integer-in-an-array/
Difficulty: Easy
Description: Given an array of integers arr, a lucky integer is an integer that has a frequency in
the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1."""

from typing import List


class Solution:
    @staticmethod
    def findLucky(arr: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        frequency = {}
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        lucky_numbers = [key for (key, value) in frequency.items() if key == value]

        return max(lucky_numbers) if lucky_numbers else -1


# Input: arr = [2, 2, 3, 4], Output: 2
assert Solution.findLucky([2, 2, 3, 4]) == 2

# Input: arr = [1, 2, 2, 3, 3, 3], Output: 3
assert Solution.findLucky([1, 2, 2, 3, 3, 3]) == 3

# Input: arr = [2, 2, 2, 3, 3], Output: -1
assert Solution.findLucky([2, 2, 2, 3, 3]) == -1

# Input: arr = [5], Output: -1
assert Solution.findLucky([5]) == -1

# Input: arr = [7, 7, 7, 7, 7, 7, 7], Output: 7
assert Solution.findLucky([7, 7, 7, 7, 7, 7, 7]) == 7

print("All unit tests are passed.")

"""3005. Count Elements With Maximum Frequency
Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
Difficulty: Easy
Description: You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the
maximum frequency.
The frequency of an element is the number of occurrences of that element in the array."""

from typing import List


class Solution:
    @staticmethod
    def maxFrequency(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize a dictionary to store the frequency of each number
        freq = {}
        max_freq = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])

        # Count the total frequencies of elements that have the maximum frequency
        return sum(freq[num] for num in freq if freq[num] == max_freq)


# Unit Test: nums = [1,2,2,3,1,4], Output = 4
assert Solution.maxFrequency([1, 2, 2, 3, 1, 4]) == 4

# Unit Test: nums = [1,2,3,4,5], Output = 5
assert Solution.maxFrequency([1, 2, 3, 4, 5]) == 5

print("All unit tests are passed")

"""697. Degree of an Array
Link: https://leetcode.com/problems/degree-of-an-array/
Difficulty: Easy
Description: Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums."""

from typing import List


class Solution:
    @staticmethod
    def findShortestSubArray(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        freq = {}
        first_last = {}  # Stores (first, last) indices for each number
        
        for i, num in enumerate(nums):
            if num not in first_last:
                first_last[num] = [i, i]  # Initialize first and last index
            else:
                first_last[num][1] = i  # Update last index
            freq[num] = freq.get(num, 0) + 1  # Update frequency
        
        # Find the maximum frequency of any one of the elements as the degree
        degree = max(freq.values())

        # Find the smallest possible length of the subarray
        return min(last - first + 1 for num, (first, last) in first_last.items() 
                   if freq[num] == degree)


def unit_tests():
    # Input: nums = [1, 2, 2, 3, 1], Output: 2
    assert Solution.findShortestSubArray([1, 2, 2, 3, 1]) == 2

    # Input: nums = [1, 2, 2, 3, 1, 4, 2], Output: 6
    assert Solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6

    # Input: nums = [1, 2, 2, 3, 1, 4, 2, 1], Output: 6
    assert Solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2, 1]) == 6


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

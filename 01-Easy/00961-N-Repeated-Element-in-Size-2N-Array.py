"""961. N-Repeated Element in Size 2N Array
Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
Difficulty: Easy
Description: You are given an integer array nums with the following properties:
nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times."""

from typing import List


class Solution:
    @staticmethod
    def repeatedNTimes(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the hash table to store the frequency of each element in the array
        freq_map = {}

        # Loop through each element in the array
        for num in nums:
            # If the element is already in the hash table, return it
            if num in freq_map:
                return num
            # Otherwise, add the element to the hash table
            freq_map[num] = 1

        # Return -1 if no element is repeated N times
        return -1


# Unit Test: Input: [1,2,3,3], Output: 3
assert Solution.repeatedNTimes([1, 2, 3, 3]) == 3

# Unit Test: Input: [2,1,2,5,3,2], Output: 2
assert Solution.repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2

# Unit Test: Input: [5,1,5,2,5,3,5,4], Output: 5
assert Solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5

print("All unit tests are passed")

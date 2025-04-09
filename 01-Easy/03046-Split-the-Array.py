"""3046. Split the Array
Link: https://leetcode.com/problems/split-the-array/
Difficulty: Easy
Description: You are given an integer array nums of even length. You have to split the
array into two parts nums1 and nums2 such that:
- nums1.length == nums2.length == nums.length / 2.
- nums1 should contain distinct elements.
- nums2 should also contain distinct elements.
Return true if it is possible to split the array, and false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def isPossibleToSplit(nums: List[int]) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the hash table
        hash_table = {}

        # Iterate through the array and count the number of occurrences
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
            # If the number of occurrences > 2, then impossible to split distinct elements
            if hash_table[num] > 2:
                return False
        return True


# Unit Test: nums = [1,1,2,2,3,4], Output = True
assert Solution.isPossibleToSplit([1, 1, 2, 2, 3, 4]) is True

# Unit Test: nums = [1,1,1,1], Output = False
assert Solution.isPossibleToSplit([1, 1, 1, 1]) is False

print("All unit tests are passed.")

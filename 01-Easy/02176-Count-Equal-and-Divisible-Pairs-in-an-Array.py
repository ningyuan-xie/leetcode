"""2176. Count Equal and Divisible Pairs in an Array
Link: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
Difficulty: Easy
Description: Given a 0-indexed integer array nums of length n and an integer k,
return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j]
and (i * j) is divisible by k."""

from typing import List


class Solution:
    @staticmethod
    def countPairs(nums: List[int], k: int) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Create a dictionary to group indices by value
        value_to_indices = {}
        for (i, num) in enumerate(nums):
            if num not in value_to_indices:
                value_to_indices[num] = []
            value_to_indices[num].append(i)
        # nums = [3,1,2,2,2,1,3] -> {3: [0, 6], 1: [1, 5], 2: [2, 3, 4]}

        count = 0
        # Iterate over grouped indices
        for indices in value_to_indices.values():
            # Check all pairs of indices for divisibility
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1

        return count


# Unit Test: nums = [3,1,2,2,2,1,3], k = 2, Output: 4
assert Solution.countPairs([3, 1, 2, 2, 2, 1, 3], 2) == 4

# Unit Test: nums = [1,2,3,4], k = 1, Output: 0
assert Solution.countPairs([1, 2, 3, 4], 1) == 0

# Unit Test: nums = [5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3], k = 7, Output: 18
assert Solution.countPairs([5, 5, 9, 2, 5, 5, 9, 2, 2, 5, 5,
                            6, 2, 2, 5, 2, 5, 4, 3], 7) == 18

print("All unit tests are passed.")

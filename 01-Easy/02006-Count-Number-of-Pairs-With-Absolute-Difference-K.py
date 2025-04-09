"""2006. Count Number of Pairs With Absolute Difference K
Link: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
Difficulty: Easy
Description: Given an integer array nums and an integer k, return the number of pairs (i, j) where
i < j such that |nums[i] - nums[j]| == k.
The value of |x| is defined as:
- x if x >= 0.
- -x if x < 0."""

from typing import List


class Solution:
    @staticmethod
    def countKDifference(nums: List[int], k: int) -> int:
        """Optimal Solution: Frequency Dictionary. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the count of pairs with absolute difference k
        count = 0
        # Initialize the frequency dict to store the frequency of each number encountered so far
        freq = {}

        for num in nums:
            # Check if there exists a number that satisfies |num - x| = k
            count += freq.get(num - k, 0)
            count += freq.get(num + k, 0)

            # Update the frequency of the current number
            freq[num] = freq.get(num, 0) + 1  # E.g. nums = [1, 2, 2, 1] -> freq = {1: 2, 2: 2}

        return count


# Unit Test: nums = [1, 2, 2, 1], k = 1, Output: 4
assert Solution.countKDifference([1, 2, 2, 1], 1) == 4

# Unit Test: nums = [1, 3], k = 3, Output: 0
assert Solution.countKDifference([1, 3], 3) == 0

# Unit Test: nums = [3, 2, 1, 5, 4], k = 2, Output: 3
assert Solution.countKDifference([3, 2, 1, 5, 4], 2) == 3

print("All unit tests are passed.")

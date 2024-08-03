# Link: https://leetcode.com/problems/maximum-average-subarray-i/
# Difficulty: Easy
# Description: You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and
# return this value. Any answer with a calculation error less than 10^-5 will be accepted.

from typing import List


class Solution:
    # Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def findMaxAverage(nums: List[int], k: int) -> float:
        # Initialize the sum of the first k elements
        max_sum = sum(nums[:k])
        current_sum = max_sum

        # Traverse the rest of the elements
        for i in range(k, len(nums)):
            # Update the current sum by adding the new element and subtracting the old element
            current_sum += nums[i] - nums[i - k]
            # Update the max sum
            max_sum = max(max_sum, current_sum)

        # Calculate the maximum average
        return max_sum / k


# Unit Test: Input: nums = [1, 12, -5, -6, 50, 3], k = 4, Output: 12.75 = (12 - 5 - 6 + 50) / 4
assert Solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75

# Unit Test: Input: nums = [5], k = 1, Output: 5.0
assert Solution.findMaxAverage([5], 1) == 5.0

# Unit Test: Input: nums = [0, 1, 1, 3, 3], k = 4, Output: 2.0
assert Solution.findMaxAverage([0, 1, 1, 3, 3], 4) == 2.0

print("All unit tests are passed")

"""3095. Shortest Subarray With OR at Least K
Link: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i
Difficulty: Easy
Description: You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty subarray of nums, or return -1 if no
special subarray exists."""

from typing import List


class Solution:
    @staticmethod
    def minimumSubarrayLength(nums: List[int], k: int) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(1)"""
        min_length = float("inf")

        # Iterate through all possible subarrays and find the minimum length
        for i in range(len(nums)):
            bitwise_or = 0
            for j in range(i, len(nums)):
                bitwise_or |= nums[j]
                if bitwise_or >= k:
                    min_length = min(min_length, j - i + 1)
                    break

        return min_length if min_length != float("inf") else -1


# Unit Test: nums = [1,2,3], k = 2, Output = 1
assert Solution.minimumSubarrayLength([1, 2, 3], 2) == 1

# Unit Test: nums = [2,1,8], k = 10, Output = 3
assert Solution.minimumSubarrayLength([2, 1, 8], 10) == 3

# Unit Test: nums = [1,2], k = 0, Output = 1
assert Solution.minimumSubarrayLength([1, 2], 0) == 1

print("All unit tests are passed.")

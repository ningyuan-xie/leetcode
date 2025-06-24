"""2760. Longest Even Odd Subarray With Threshold
Link: https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums and an integer threshold.
Find the length of the longest subarray of nums starting at index l and ending at index r
(0 <= l <= r < nums.length) that satisfies the following conditions:
- nums[l] % 2 == 0
- For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
- For all indices i in the range [l, r], nums[i] <= threshold
Return an integer denoting the length of the longest such subarray.
Note: A subarray is a contiguous non-empty sequence of elements within an array."""

from typing import List


class Solution:
    @staticmethod
    def longestAlternatingSubarray(nums: List[int], threshold: int) -> int:
        """Sub-Optimal Solution: Brute Force. Time Complexity: O(n^3), Space Complexity: O(1)."""
        # Initialize the maximum length
        max_length = 0
        n = len(nums)

        def is_alternating_subarray(left: int, right: int) -> bool:
            """Helper function to check if the subarray is alternating"""
            for i in range(left, right):
                if nums[i] % 2 == nums[i + 1] % 2:
                    return False
            return True

        # Check each subarray to see if it satisfies the three conditions
        for l in range(n):
            for r in range(l, n):
                if (nums[l] % 2 == 0
                        and is_alternating_subarray(l, r)
                        and all(nums[i] <= threshold for i in range(l, r + 1))):
                    max_length = max(max_length, r - l + 1)

        return max_length

    @staticmethod
    def longestAlternatingSubarraySlidingWindow(nums: List[int], threshold: int) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)."""
        max_length = 0
        n = len(nums)

        # O(n) sliding window here: i never resets to a previous position
        i = 0
        while i < n:
            if nums[i] % 2 == 0 and nums[i] <= threshold:  # Start only at even numbers within threshold
                length = 1

                # Expand the alternating subarray
                while i + 1 < n and nums[i + 1] % 2 != nums[i] % 2 and nums[i + 1] <= threshold:
                    length += 1
                    i += 1  # Move to next

                max_length = max(max_length, length)
            i += 1  # Move to next potential start

        return max_length


# Input: nums = [3,2,5,4], threshold = 5, Output: 3
assert Solution.longestAlternatingSubarraySlidingWindow([3, 2, 5, 4], 5) == 3

# Input: nums = [1,2], threshold = 2, Output: 1
assert Solution.longestAlternatingSubarraySlidingWindow([1, 2], 2) == 1

# Input: nums = [2,3,4,5], threshold = 4, Output: 3
assert Solution.longestAlternatingSubarraySlidingWindow([2, 3, 4, 5], 4) == 3

print("All unit tests are passed.")

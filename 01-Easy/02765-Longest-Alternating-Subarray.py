"""2765. Longest Alternating Subarray
Link: https://leetcode.com/problems/longest-alternating-subarray/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums. A subarray s of length m is called
alternating if:
- m is greater than 1.
- s1 = s0 + 1.
- The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words,
s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.
Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.
A subarray is a contiguous non-empty sequence of elements within an array."""

from typing import List


class Solution:
    @staticmethod
    def alternatingSubarray(nums: List[int]) -> int:
        """Sub-Optimal Solution: Brute Force. Time Complexity: O(n^3), Space Complexity: O(1)"""
        # Initialize the maximum length
        max_length = -1
        n = len(nums)

        def is_alternating_subarray(left: int, right: int) -> bool:
            """Helper function to check if the subarray is alternating"""
            sign = 1  # Start with a positive difference
            for i in range(left, right):
                if (nums[i + 1] - nums[i]) * sign != 1:
                    return False
                sign *= -1  # Flip expected sign
            return True

        # Check each subarray to see if it satisfies the three conditions
        for l in range(n):
            for r in range(l + 1, n):  # The subarray must have at least two elements
                if is_alternating_subarray(l, r):
                    max_length = max(max_length, r - l + 1)

        return max_length

    @staticmethod
    def alternatingSubarraySlidingWindow(nums: List[int]) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)"""
        n = len(nums)
        max_length = -1  # Default if no valid subarray is found

        # O(n) sliding window here: i never resets to a previous position
        i = 0
        while i < n - 1:
            if nums[i] + 1 == nums[i + 1]:  # Found a valid start
                length = 2  # At least [nums[i], nums[i+1]]

                # Expand the alternating subarray
                while i + 2 < n and nums[i + 2] - nums[i + 1] == -1 * (nums[i + 1] - nums[i]):
                    length += 1
                    i += 1  # Move to next

                max_length = max(max_length, length)
            i += 1  # Move to next potential start

        return max_length


# Unit Test: nums = [2,3,4,3,4], Output: 4
assert Solution.alternatingSubarraySlidingWindow([2, 3, 4, 3, 4]) == 4

# Unit Test: nums = [4,5,6], Output: 2
assert Solution.alternatingSubarraySlidingWindow([4, 5, 6]) == 2

# Unit Test: nums = [21,9,5], Output: -1
assert Solution.alternatingSubarraySlidingWindow([21, 9, 5]) == -1

# Unit Test: nums = [1,2,3,4], Output: 2
assert Solution.alternatingSubarraySlidingWindow([1, 2, 3, 4]) == 2

print("All unit tests are passed.")

"""1588. Sum of All Odd Length Subarrays
Link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
Difficulty: Easy
Description: Given an array of positive integers arr, calculate the sum of all possible odd-length
subarrays.
A subarray is a contiguous subsequence of the array."""

from typing import List


class Solution:
    @staticmethod
    def sumOddLengthSubarrays(arr: List[int]) -> int:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the sum of all odd-length subarrays
        odd_length_subarray_sum = 0

        # Calculate the prefix sum of the array
        prefix_sum = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            # E.g. arr = [1, 4, 2, 5, 3], prefix_sum = [0, 1, 5, 7, 12, 15]
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        # Outer loop: iterate through each possible starting index for subarrays
        for i in range(len(arr)):
            # Inner loop: select the ending index for odd-length subarrays
            # The range(i, len(arr), 2) ensures only odd-length subarrays by incrementing by 2
            for j in range(i, len(arr), 2):
                # prefix_sum[j+1] - prefix_sum[i] gives the sum of the subarray arr[i:j+1]
                odd_length_subarray_sum += prefix_sum[j + 1] - prefix_sum[i]

        return odd_length_subarray_sum


# Input: arr = [1, 4, 2, 5, 3], Output: 58
assert Solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]) == 58

# Input: arr = [1, 2], Output: 3
assert Solution.sumOddLengthSubarrays([1, 2]) == 3

# Input: arr = [10, 11, 12], Output: 66
assert Solution.sumOddLengthSubarrays([10, 11, 12]) == 66

print("All unit tests are passed.")

"""2970. Count the Number of Incremovable Subarrays I
Link: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays/
Difficulty: Easy
Description: You are given a 0-indexed array of positive integers nums.
A subarray of nums is called incremovable if nums becomes strictly increasing on removing the
subarray. For example, the subarray [3, 4] is an incremovable subarray of [5, 3, 4, 6, 7] because
removing this subarray changes the array [5, 3, 4, 6, 7] to [5, 6, 7] which is strictly increasing.
Return the total number of incremovable subarrays of nums.
Note that an empty array is considered strictly increasing.
A subarray is a contiguous non-empty sequence of elements within an array."""

from typing import List


class Solution:
    @staticmethod
    def incremovableSubarrayCount(nums: List[int]) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(1)."""
        n = len(nums)
        count = 0

        def isStrictlyIncreasing(array: List[int]) -> bool:
            """Helper function to check if the array is strictly increasing"""
            return all(array[index] < array[index + 1] for index in range(len(array) - 1))

        for i in range(n):
            for j in range(i, n):
                # Check if remove the subarray makes nums strictly increasing
                if isStrictlyIncreasing(nums[:i] + nums[j + 1:]):
                    count += 1
        return count


# Unit Test: nums = [1,2,3,4], Output: 10
assert Solution.incremovableSubarrayCount([1, 2, 3, 4]) == 10

# Unit Test: nums = [6,5,7,8], Output: 7
assert Solution.incremovableSubarrayCount([6, 5, 7, 8]) == 7

# Unit Test: nums = [8,7,6,6], Output:3
assert Solution.incremovableSubarrayCount([8, 7, 6, 6]) == 3

print("All unit tests are passed.")

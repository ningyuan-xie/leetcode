"""3471. Find the Largest Almost Missing Integer
Link: https://leetcode.com/problems/find-the-largest-almost-missing-integer/
Difficulty: Easy
Description: You are given an integer array nums and an integer k.
An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.
Return the largest almost missing integer from nums. If no such integer exists, return -1.
A subarray is a contiguous sequence of elements within an array."""

from typing import List


class Solution:
    @staticmethod
    def findLargest(nums: List[int], k: int) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(nums)
        # If the length of nums is equal to k, return the largest element
        if n == k:
            return max(nums)

        # Initialize a dictionary to count the frequency of each number
        count = {}
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            for num in subarray:
                count[num] = count.get(num, 0) + 1

        # Find the largest almost missing integer
        largest_almost_missing = -1
        for num in count:
            if count[num] == 1:
                largest_almost_missing = max(largest_almost_missing, num)
        return largest_almost_missing if largest_almost_missing != -1 else -1


def unit_tests():
    # Input: nums = [3,9,2,1,7], k = 3, Output: 7
    assert Solution.findLargest([3, 9, 2, 1, 7], 3) == 7

    # Input: nums = [3,9,7,2,1,7], k = 4, Output: 3
    assert Solution.findLargest([3, 9, 7, 2, 1, 7], 4) == 3

    # Input: nums = [0,0], k = 1, Output: -1
    assert Solution.findLargest([0, 0], 1) == -1

    # Input: nums = [0,0], k = 2, Output: 0
    assert Solution.findLargest([0, 0], 2) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

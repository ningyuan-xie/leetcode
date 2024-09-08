"""1005. Maximize Sum Of Array After K Negations
Link: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations
Difficulty: Easy
Description: Given an integer array nums and an integer k, modify the array in the following way:
choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.
Return the largest possible sum of the array after modifying it in this way."""

from typing import List


class Solution:
    @staticmethod
    def largestSumAfterKNegations(nums: List[int], k: int) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(n), Space Complexity: O(1).
           The solution uses a greedy approach by sorting the array and negating the
           smallest element"""
        # Sort the array to find the smallest element
        nums.sort()  # E.g. nums = [4, 2, 3] -> [2, 3, 4]

        # Greedy approach: flip the most negative numbers first
        i = 0
        while i < len(nums) and nums[i] < 0 < k:
            nums[i] = -nums[i]  # flip the most negative number
            i += 1
            k -= 1

        # Greedy approach: if more k left, minimize the penalty by flipping the smallest number
        if k > 0 and k % 2 == 1:
            # Sort the array again
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)


# Unit Test: nums = [4, 2, 3], k = 1, Output: 5
assert Solution.largestSumAfterKNegations([4, 2, 3], 1) == 5

# Unit Test: nums = [3, -1, 0, 2], k = 3, Output: 6
assert Solution.largestSumAfterKNegations([3, -1, 0, 2], 3) == 6

# Unit Test: nums = [2, -3, -1, 5, -4], k = 2, Output: 13
assert Solution.largestSumAfterKNegations([2, -3, -1, 5, -4], 2) == 13

print("All unit tests are passed")

"""1005. Maximize Sum Of Array After K Negations
Link: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations
Difficulty: Easy
Description: Given an integer array nums and an integer k, modify the array in the following way:
• choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.
Return the largest possible sum of the array after modifying it in this way."""

from typing import List


class Solution:
    @staticmethod
    def largestSumAfterKNegations(nums: List[int], k: int) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(nlogn), Space Complexity: O(1)."""
        # Sort the array to find the smallest elements
        nums.sort()
        
        # First pass: negate all negative numbers while we have k operations left
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
                
        # Second pass: if k is odd, negate the smallest remaining number
        if k % 2 == 1:
            min_idx = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[min_idx]:
                    min_idx = i
            nums[min_idx] = -nums[min_idx]
            
        return sum(nums)


def unit_tests():
    # Unit Test: nums = [4, 2, 3], k = 1, Output: 5
    assert Solution.largestSumAfterKNegations([4, 2, 3], 1) == 5

    # Unit Test: nums = [3, -1, 0, 2], k = 3, Output: 6
    assert Solution.largestSumAfterKNegations([3, -1, 0, 2], 3) == 6

    # Unit Test: nums = [2, -3, -1, 5, -4], k = 2, Output: 13
assert Solution.largestSumAfterKNegations([2, -3, -1, 5, -4], 2) == 13


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

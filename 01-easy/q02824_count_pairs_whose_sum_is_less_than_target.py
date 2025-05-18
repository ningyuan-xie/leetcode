"""2824. Count Pairs Whose Sum is Less than Target
Link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
Difficulty: Easy
Description: Given a 0-indexed integer array nums of length n and an integer target, return the number
of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target."""

from typing import List


class Solution:
    @staticmethod
    def countPairs(nums: List[int], target: int) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        # Sort the array
        nums.sort()
        # Initialize the count of pairs
        count = 0
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                # If the sum of the two numbers is less than the target, then all the pairs
                # from left to right will be less than the target
                count += right - left
                left += 1
            else:
                right -= 1
        return count


# Unit Test: nums = [-1,1,2,3,1], target = 2, Output: 3
assert Solution.countPairs([-1, 1, 2, 3, 1], 2) == 3

# Unit Test: nums = [-6,2,5,-2,-7,-1,3], target = -2, Output: 10
assert Solution.countPairs([-6, 2, 5, -2, -7, -1, 3], -2) == 10

print("All unit tests are passed.")

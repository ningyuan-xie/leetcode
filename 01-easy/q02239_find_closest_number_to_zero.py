"""2239. Find Closest Number to Zero
Link: https://leetcode.com/problems/find-closest-number-to-zero/
Difficulty: Easy
Description: Given an integer array nums of size n, return the number with the value closest to 0 in
nums. If there are multiple answers, return the number with the largest value."""

from typing import List


class Solution:
    @staticmethod
    def findClosestNumber(nums: List[int]) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        closest_number = float("inf")

        # Update if closer to zero or if there's a tie and num > closest
        for num in nums:
            if (abs(num) < abs(closest_number)
                    or (abs(num) == abs(closest_number) and num > closest_number)):
                closest_number = num

        return closest_number


# Input: nums = [-4,-2,1,4,8], Output: 1
assert Solution.findClosestNumber([-4, -2, 1, 4, 8]) == 1

# Input: nums = [2,-1,1], Output: 1
assert Solution.findClosestNumber([2, -1, 1]) == 1

print("All unit tests are passed.")

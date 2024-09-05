"""976. Largest Perimeter Triangle
Link: https://leetcode.com/problems/largest-perimeter-triangle/
Difficulty: Easy
Description: Given an array nums of positive integers, return the largest perimeter of a triangle
with a non-zero area, formed from 3 of these lengths. If it is impossible to form any triangle of
a non-zero area, return 0."""

from typing import List


class Solution:
    @staticmethod
    def largestPerimeter(nums: List[int]) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(nlog(n)), Space Complexity: O(1)
           The solution uses a greedy approach by sorting the array in descending order and
           checking the sum of the two smaller sides against the largest side"""
        # Sort the array in descending order
        nums.sort(reverse=True)

        # Greedy approach: start from the largest side
        for i in range(len(nums) - 2):
            # If the largest side < sum of the two smaller sides, return the perimeter
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]

        # Return 0 if no triangle can be formed
        return 0


# Unit Test: Input: [2,1,2], Output: 5
assert Solution.largestPerimeter([2, 1, 2]) == 5

# Unit Test: Input: [1,2,1], Output: 0
assert Solution.largestPerimeter([1, 2, 1]) == 0

# Unit Test: Input: [3,2,3,4], Output: 10
assert Solution.largestPerimeter([3, 2, 3, 4]) == 10

# Unit Test: Input: [3,6,2,3], Output: 8
assert Solution.largestPerimeter([3, 6, 2, 3]) == 8

print("All unit tests are passed")

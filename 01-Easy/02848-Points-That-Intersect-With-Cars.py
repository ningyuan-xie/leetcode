"""2848. Points That Intersect With Cars
Link: https://leetcode.com/problems/points-that-intersect-the-cars/
Difficulty: Easy
Description: You are given a 0-indexed 2D integer array nums representing the coordinates of the cars
parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point
of the ith car and endi is the ending point of the ith car.
Return the number of integer points on the line that are covered with any part of a car."""

from typing import List


class Solution:
    @staticmethod
    def numberOfPoints(nums: List[List[int]]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the set of points
        points = set()

        # Add all the points to the set
        for start, end in nums:
            for point in range(start, end + 1):
                points.add(point)

        return len(points)


# Unit Test: nums = [[3,6],[1,5],[4,7]], Output: 7
assert Solution.numberOfPoints([[3, 6], [1, 5], [4, 7]]) == 7

# Unit Test: nums = [[1,3],[5,8]], Output: 7
assert Solution.numberOfPoints([[1, 3], [5, 8]]) == 7

print("All unit tests are passed")

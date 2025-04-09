"""1637. Widest Vertical Area Between Two Points Containing No Points
Link: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
Difficulty: Easy
Description: Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area
between two points such that no points are inside the area.
A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite
height). The widest vertical area is the one with the maximum width.
Note that points on the edge of a vertical area are not considered included in the area."""

from typing import List


class Solution:
    @staticmethod
    def maxWidthOfVerticalArea(points: List[List[int]]) -> int:
        """Optimal Solution: Sort and Find Maximum Difference.
           Time Complexity: O(nlog(n)), Space Complexity: O(n)"""
        # Sort the points by x-coordinate (y-coordinates are not useful)
        points.sort()  # [[8, 7], [9, 9], [7, 4], [9, 7]] -> [[7, 4], [8, 7], [9, 7], [9, 9]]

        # Find the maximum difference between adjacent x-coordinates (y-coordinates are not useful)
        max_width = 0
        for i in range(1, len(points)):
            max_width = max(max_width, points[i][0] - points[i - 1][0])

        return max_width


# Unit Test: points = [[8, 7], [9, 9], [7, 4], [9, 7]], Output: 1
assert Solution.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]) == 1

# Unit Test: points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]], Output: 3
assert Solution.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3

print("All unit tests are passed.")

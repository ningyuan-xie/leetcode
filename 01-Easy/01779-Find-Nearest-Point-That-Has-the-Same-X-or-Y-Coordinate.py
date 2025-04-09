"""1779. Find Nearest Point That Has the Same X or Y Coordinate
Link: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
Difficulty: Easy
Description: You are given two integers, x and y, which represent your current location on a
Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents
that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same
y-coordinate as your location.
Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your
current location. If there are multiple, return the valid point with the smallest index. If
there are no valid points, return -1.
The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2)."""

from typing import List


class Solution:
    @staticmethod
    def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
        """Optimal Solution: Manhattan Distance. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the minimum distance and the index of the nearest valid point
        min_distance = float("inf")
        nearest_index = -1

        # Check each point to see if it has the same x or y coordinate as the current location
        for i, (xi, yi) in enumerate(points):
            if xi == x or yi == y:
                # Calculate the Manhattan distance between the current location and the point
                distance = abs(xi - x) + abs(yi - y)
                # Update the minimum distance and the index of the nearest valid point
                if distance < min_distance:
                    min_distance = distance
                    nearest_index = i

        return nearest_index


# Unit Test: x = 3, y = 4, points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]], Output: 2
assert Solution.nearestValidPoint(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]) == 2

# Unit Test: x = 3, y = 4, points = [[3, 4]], Output: 0
assert Solution.nearestValidPoint(3, 4, [[3, 4]]) == 0

# Unit Test: x = 3, y = 4, points = [[2, 3]], Output: -1
assert Solution.nearestValidPoint(3, 4, [[2, 3]]) == -1

print("All unit tests are passed.")

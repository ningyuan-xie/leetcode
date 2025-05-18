"""812. Largest Triangle Area
Link: https://leetcode.com/problems/largest-triangle-area/
Difficulty: Easy
Description: You have a list of points in the plane. Return the area of the largest triangle
that can be formed by any 3 of the points."""

from typing import List


class Solution:
    @staticmethod
    def largestTriangleArea(points: List[List[int]]) -> float:
        """Optimal Solution: Shoelace Formula. Time Complexity: O(n^3), Space Complexity: O(1)."""
        # Initialize the maximum area
        max_area = 0

        def area(p1: List[int], p2: List[int], p3: List[int]) -> float:
            """Helper function: Calculate the area of a triangle using the
               Shoelace Formula: 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|"""
            # Extract the coordinates of the points
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            # Calculate the area of the triangle
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        # Enumerate all possible triangles
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    # Calculate the area of the current triangle
                    current_area = area(points[i], points[j], points[k])
                    # Update the maximum area
                    max_area = max(max_area, current_area)

        return max_area


# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]], Output: 2.0
assert Solution.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]) == 2.0

# Input: points = [[1,0],[0,0],[0,1]], Output: 0.5
assert Solution.largestTriangleArea([[1, 0], [0, 0], [0, 1]]) == 0.5

# Input: points = [[1,1],[2,2],[3,3]], Output: 0.0
assert Solution.largestTriangleArea([[1, 1], [2, 2], [3, 3]]) == 0.0

print("All unit tests are passed.")

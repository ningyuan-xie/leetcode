"""883. Projection Area of 3D Shapes
Link: https://leetcode.com/problems/projection-area-of-3d-shapes/
Difficulty: Easy
Description: You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned
with the x, y, and z axes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).
We view the projection of these cubes onto the xy, yz, and zx planes.
A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. W
e are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
Return the total area of all three projections."""

from typing import List


class Solution:
    @staticmethod
    def projectionArea(grid: List[List[int]]) -> int:
        """Optimal Solution: Generator Expression & Matrix Transposition.
           Time Complexity: O(n^2), Space Complexity: O(1)"""
        # Top view is viewing from above
        top_view = sum(v > 0 for row in grid for v in row)

        # Front view is standing in front of the grid
        # [[1, 2], [3, 4]]: can only see 2 and 4, so 6
        front_view = sum(max(row) for row in grid)

        # Side view is standing on the side of the grid: can only see 3 and 4, so 7
        # *grid unpacks the grid: [[1, 2], [3, 4]] -> [1, 2], [3, 4]
        # zip() combines each element into tuples: [1, 2], [3, 4] -> [(1, 3), (2, 4)]
        side_view = sum(max(col) for col in zip(*grid))

        return top_view + front_view + side_view


# Unit Test: Input: grid = [[1,2],[3,4]], Output: 17
assert Solution.projectionArea([[1, 2], [3, 4]]) == 17

# Unit Test: Input: grid = [[2]], Output: 5
assert Solution.projectionArea([[2]]) == 5

# Unit Test: Input: grid = [[1,2],[0,0]], Output: 7
assert Solution.projectionArea([[1, 2], [0, 0]]) == 7

# Unit Test: Input: grid = [[1,0],[0,2]], Output: 8
assert Solution.projectionArea([[1, 0], [0, 2]]) == 8

# Unit Test: Input: grid = [[1,1,1],[1,0,1],[1,1,1]], Output: 14
assert Solution.projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 14

print("All unit tests are passed")

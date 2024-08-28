"""892. Surface Area of 3D Shapes
Link: https://leetcode.com/problems/surface-area-of-3d-shapes/
Difficulty: Easy
Description: You are given an n x n grid where you have placed some 1 x 1 x 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
After placing these cubes, you have decided to glue any directly adjacent cubes to each other,
forming several irregular 3D shapes.
Return the total surface area of the resulting shapes.
Note: The bottom face of each shape counts toward its surface area."""

from typing import List


class Solution:
    @staticmethod
    def surfaceArea(grid: List[List[int]]) -> int:
        """Optimal Solution: Math. Time Complexity: O(n^2), Space Complexity: O(1).
           Similar to 0463-Island-Perimeter.py and 0883-Projection-Area-of-3D-Shapes.py"""
        # Initialize the total surface area
        total_area = 0

        # Traverse each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Skip the cell with 0 cube
                if grid[i][j] == 0:
                    continue
                # Calculate the surface area of the cell: 4 sides + top + bottom
                cell_area = 4 * grid[i][j] + 2
                # Subtract the overlapped area with the cell on the left
                if i > 0:
                    cell_area -= 2 * min(grid[i][j], grid[i - 1][j])
                # Subtract the overlapped area with the cell on the top (not 3D top, 2D top)
                if j > 0:
                    cell_area -= 2 * min(grid[i][j], grid[i][j - 1])
                # Add the surface area of the cell to the total surface area
                total_area += cell_area

        return total_area


# Unit Test: Input: grid = [[2]], Output: 10
assert Solution.surfaceArea([[2]]) == 10

# Unit Test: Input: grid = [[1,2],[3,4]], Output: 34
assert Solution.surfaceArea([[1, 2], [3, 4]]) == 34

# Unit Test: Input: grid = [[1,0],[0,2]], Output: 16
assert Solution.surfaceArea([[1, 0], [0, 2]]) == 16

# Unit Test: Input: grid = [[1,1,1],[1,0,1],[1,1,1]], Output: 32
assert Solution.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 32

print("All unit tests are passed")

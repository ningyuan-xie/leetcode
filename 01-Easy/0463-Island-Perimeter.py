# Link: https://leetcode.com/problems/island-perimeter/
# Difficulty: Easy
# Description: You are given a map in form of a two-dimensional integer grid where 1 represents land
# and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island
# (i.e., one or more connected land cells).
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

from typing import List


class Solution:
    # Optimal Solution: Counting Edges. Time Complexity: O(m * n), Space Complexity: O(1)
    @staticmethod
    def islandPerimeter(grid: List[List[int]]) -> int:
        perimeter = 0
        # Outer loop: Iterate through the rows
        for i in range(len(grid)):  # E.g. i = 0, 1, 2, 3
            # Inner loop: Iterate through the columns
            for j in range(len(grid[0])):  # E.g. j = 0, 1, 2, 3
                # If the cell is land
                if grid[i][j] == 1:
                    # Increment the perimeter by 4
                    perimeter += 4
                    # Check the cell above
                    if i > 0 and grid[i - 1][j] == 1:
                        # Subtract 2 from the perimeter since the top and current cells share an edge
                        perimeter -= 2
                    # Check the cell to the left
                    if j > 0 and grid[i][j - 1] == 1:  # Check the cell to the left
                        # Subtract 2 from the perimeter since the left and current cells share an edge
                        perimeter -= 2
        return perimeter

    # Optimal Solution: Recursive DFS. Time Complexity: O(m * n), Space Complexity: O(m * n)
    @staticmethod
    def islandPerimeterDFS(grid: List[List[int]]) -> int:
        visited = set()  # Memory Complexity: O(m * n)

        # Helper function: DFS
        def dfs(y_axis: int, x_axis: int) -> int:
            # Base Case: If the current cell is out of bounds or water, we have an edge = 1
            if (y_axis < 0 or y_axis >= len(grid)   # Out of upper or lower bounds
                    or x_axis < 0 or x_axis >= len(grid[0])   # Out of left or right bounds
                    or grid[y_axis][x_axis] == 0):  # Water
                return 1
            # Base Case: If the cell is already visited before, ignore it
            if (y_axis, x_axis) in visited:
                return 0
            # Mark the current cell as visited
            visited.add((y_axis, x_axis))
            # Recursive Case: Explore the current cell's neighbors: Up, Down, Left, and Right
            return (dfs(y_axis - 1, x_axis) + dfs(y_axis + 1, x_axis) +
                    dfs(y_axis, x_axis - 1) + dfs(y_axis, x_axis + 1))

        # Outer loop: Iterate through the rows
        for i in range(len(grid)):
            # Inner loop: Iterate through the columns
            for j in range(len(grid[0])):
                # If the current cell is land
                if grid[i][j] == 1:
                    # Start DFS from the current cell
                    return dfs(y_axis=i, x_axis=j)


# Unit Test: Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
assert Solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16

# Unit Test: Input: grid = [[1]], Output: 4
assert Solution.islandPerimeterDFS([[1]]) == 4

# Unit Test: Input: grid = [[1, 0]], Output: 4
assert Solution.islandPerimeterDFS([[1, 0]]) == 4

print("All unit tests are passed")

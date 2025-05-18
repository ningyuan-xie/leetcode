"""463. Island Perimeter
Link: https://leetcode.com/problems/island-perimeter/
Difficulty: Easy
Description: You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island."""

from typing import List


class Solution:
    @staticmethod
    def islandPerimeter(grid: List[List[int]]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(m * n), Space Complexity: O(1)."""
        # Initialize perimeter
        perimeter = 0

        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the cell is land (1)
                if grid[i][j] == 1:
                    perimeter += 4

                    # Subtract 2 for the cell above
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    # Subtract 2 for the cell to the left
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter


def unit_tests():
    # Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    assert Solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16

    # Input: grid = [[1]], Output: 4
    assert Solution.islandPerimeter([[1]]) == 4

    # Input: grid = [[1, 0]], Output: 4
    assert Solution.islandPerimeter([[1, 0]]) == 4


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

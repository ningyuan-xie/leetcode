"""3142. Check if Grid Satisfies Conditions
Link: https://leetcode.com/problems/check-if-grid-satisfies-conditions
Difficulty: Easy
Description: You are given a 2D matrix grid of size m x n. You need to check if each cell
grid[i][j] is:
- Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
- Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return true if all the cells satisfy these conditions, otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def checkGrid(grid: List[List[int]]) -> bool:
        """Optimal Solution: Matrix Manipulation. Time Complexity: O(m*n), Space Complexity: O(1)"""
        rows, cols = len(grid), len(grid[0])

        def is_valid(i: int, j: int) -> bool:
            """Helper function to check the conditions for each cell"""
            # Check if the cell below exists and is equal
            if i + 1 < rows and grid[i][j] != grid[i + 1][j]:
                return False
            # Check if the cell to the right exists and is different
            if j + 1 < cols and grid[i][j] == grid[i][j + 1]:
                return False
            return True

        # Iterate through each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # If any cell does not satisfy the conditions, return False
                if not is_valid(row, col):
                    return False
        return True


# Unit Test: grid = [[1,0,2],[1,0,2]], Output = True
assert Solution.checkGrid([[1, 0, 2], [1, 0, 2]]) is True

# Unit Test: grid = [[1,1,1],[0,0,0]], Output = False
assert Solution.checkGrid([[1, 1, 1], [0, 0, 0]]) is False

# Unit Test: grid = [[1],[2],[3]], Output = False
assert Solution.checkGrid([[1], [2], [3]]) is False

print("All unit tests are passed")

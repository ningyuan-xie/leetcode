"""2319. Check if Matrix Is X Matrix
Link: https://leetcode.com/problems/check-if-matrix-is-x-matrix/
Difficulty: Easy
Description: A square matrix is said to be an X-Matrix if both of the following conditions hold:
1. All the elements in the diagonals of the matrix are non-zero.
2. All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an
X-Matrix. Otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def checkXMatrix(grid: List[List[int]]) -> bool:
        """Optimal Solution: Matrix Traversal. Time Complexity: O(n), Space Complexity: O(1)"""
        n = len(grid)

        # Check the diagonals: All elements must be non-zero
        for i in range(n):
            if grid[i][i] == 0 or grid[i][n - 1 - i] == 0:
                return False

        # Check the other elements: All elements must be zero
        for i in range(n):
            for j in range(n):
                if i != j and j != n - 1 - i and grid[i][j] != 0:
                    return False

        return True


# Unit Test: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]], Output: True
assert Solution.checkXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]) is True

# Unit Test: grid = [[5,7,0],[0,3,1],[0,5,0]], Output: False
assert Solution.checkXMatrix([[5, 7, 0], [0, 3, 1], [0, 5, 0]]) is False

print("All unit tests are passed")

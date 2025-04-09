"""3242. Design Neighbor Sum Service
Link: https://leetcode.com/problems/design-neighbor-sum-service
Difficulty: Easy
Description: You are given a n x n 2D array grid containing distinct elements in the range
[0, n2 - 1].
Implement the NeighborSum class:
- NeighborSum(int [][]grid) initializes the object.
- int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value,
that is either to the top, left, right, or bottom of value in grid.
- int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value,
that is either to the top-left, top-right, bottom-left, or bottom-right of value in grid."""

from typing import List


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        """Initialize the NeighborSum with a grid of neighbors."""
        self.n = len(grid)
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        """Calculate the sum of adjacent neighbors."""
        # Find the coordinates of the value in the grid
        x, y = next((i, j) for i in range(self.n) for j in range(self.n)
                    if self.grid[i][j] == value)

        # Calculate the sum of adjacent neighbors
        adjacent_sum = 0
        adjacent_sum += self.grid[x][y - 1] if y > 0 else 0  # left
        adjacent_sum += self.grid[x][y + 1] if y < self.n - 1 else 0  # right
        adjacent_sum += self.grid[x - 1][y] if x > 0 else 0  # top
        adjacent_sum += self.grid[x + 1][y] if x < self.n - 1 else 0  # bottom
        return adjacent_sum

    def diagonalSum(self, value: int) -> int:
        """Calculate the sum of diagonal neighbors."""
        # Find the coordinates of the value in the grid
        x, y = next((i, j) for i in range(self.n) for j in range(self.n)
                    if self.grid[i][j] == value)

        # Calculate the sum of diagonal neighbors
        diagonal_sum = 0
        diagonal_sum += self.grid[x - 1][y - 1] \
            if x > 0 and y > 0 else 0  # top-left
        diagonal_sum += self.grid[x - 1][y + 1] \
            if x > 0 and y < self.n - 1 else 0  # top-right
        diagonal_sum += self.grid[x + 1][y - 1] \
            if x < self.n - 1 and y > 0 else 0  # bottom-left
        diagonal_sum += self.grid[x + 1][y + 1] \
            if x < self.n - 1 and y < self.n - 1 else 0  # bottom-right
        return diagonal_sum


# Unit Test: Input: ["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]
# [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]
# Output: [null, 6, 16, 16, 4]
ns = NeighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
assert ns.adjacentSum(1) == 6
assert ns.adjacentSum(4) == 16
assert ns.diagonalSum(4) == 16
assert ns.diagonalSum(8) == 4

# Unit Test: Input: ["NeighborSum", "adjacentSum", "diagonalSum"]
# [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]
# Output: [null, 23, 45]
ns = NeighborSum([[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]])
assert ns.adjacentSum(15) == 23
assert ns.diagonalSum(9) == 45

print("All unit tests are passed")

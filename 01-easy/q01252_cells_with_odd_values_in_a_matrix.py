"""1252. Cells with Odd Values in a Matrix
Link: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
Difficulty: Easy
Description: There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
For each location indices[i], do both of the following:
1. Increment all the cells on row ri.
2. Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices."""

from typing import List


class Solution:
    @staticmethod
    def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
        """Optimal Solution: Matrix Manipulation. Time Complexity: O(m*n), Space Complexity: O(m*n)."""
        # Initialize matrix with 0s
        row, col = m, n
        matrix = [[0] * n for _ in range(m)]
        
        # Increment rows and columns based on indices
        for ri, ci in indices:
            for i in range(row):
                matrix[i][ci] += 1
            for i in range(col):
                matrix[ri][i] += 1
        
        # Count odd cells
        odd_count = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] % 2 == 1:
                    odd_count += 1

        return odd_count


def unit_tests():
    # Input: m = 2, n = 3, indices = [[0, 1], [1, 1]], Output: 6
    assert Solution.oddCells(2, 3, [[0, 1], [1, 1]]) == 6

    # Input: m = 2, n = 2, indices = [[1, 1], [0, 0]], Output: 0
    assert Solution.oddCells(2, 2, [[1, 1], [0, 0]]) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

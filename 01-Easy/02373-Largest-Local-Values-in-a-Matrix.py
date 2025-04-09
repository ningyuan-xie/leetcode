"""2373. Largest Local Values in a Matrix
Link: https://leetcode.com/problems/largest-local-values-in-a-matrix/
Difficulty: Easy
Description: You are given an n x n integer matrix grid.
Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
- maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1
and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
Return the generated matrix."""

from typing import List


class Solution:
    @staticmethod
    def largestLocal(grid: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(1).
           This is the Max Pooling operation in CNN"""
        result = [[0] * (len(grid) - 2) for _ in range(len(grid) - 2)]

        def get_max_3x3(center_x: int, center_y: int) -> int:
            """Helper function to get the maximum value in the 3x3 submatrix centered at (x, y)"""
            return max(grid[x][y] for x in range(center_x - 1, center_x + 2)
                       for y in range(center_y - 1, center_y + 2))

        # Start with the 2nd row and 2nd column to the second last row and second last column
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                result[i - 1][j - 1] = get_max_3x3(i, j)
        return result


# Unit Test: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]], Output: [[9,9],[8,6]]
assert (Solution.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])
        == [[9, 9], [8, 6]])

# Unit Test: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]],
# Output: [[2,2,2],[2,2,2],[2,2,2]]
assert (Solution.largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1],
                               [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
        == [[2, 2, 2], [2, 2, 2], [2, 2, 2]])

print("All unit tests are passed.")

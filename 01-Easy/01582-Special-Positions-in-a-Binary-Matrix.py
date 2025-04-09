"""1582. Special Positions in a Binary Matrix
Link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/
Difficulty: Easy
Description: Given an m x n binary matrix mat, return the number of special positions in mat.
A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j
are 0 (rows and columns are 0-indexed)."""

from typing import List


class Solution:
    @staticmethod
    def numSpecial(mat: List[List[int]]) -> int:
        """Optimal Solution: Matrix Traversal. Time Complexity: O(n^2), Space Complexity: O(1)"""
        # Initialize the number of special positions
        special_positions = 0

        # Iterate through the matrix and check each row and column
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    # Check if the current row and column are special
                    if (sum(mat[i]) == 1 and
                            sum([mat[row][j] for row in range(len(mat))]) == 1):
                        special_positions += 1

        return special_positions


# Unit Test: mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]], Output: 1
assert Solution.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]) == 1

# Unit Test: mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]], Output: 3
assert Solution.numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3

# Unit Test: mat = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]], Output: 2
assert Solution.numSpecial([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 2

print("All unit tests are passed")

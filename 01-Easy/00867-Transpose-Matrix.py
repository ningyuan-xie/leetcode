"""867. Transpose Matrix
Link: https://leetcode.com/problems/transpose-matrix/
Difficulty: Easy
Description: Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row
and column indices."""

from typing import List


class Solution:
    @staticmethod
    def transpose(matrix: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: Brute Force. Time Complexity: O(n*m), Space Complexity: O(n*m)."""
        # Get the number of rows and columns of the matrix
        rows, cols = len(matrix), len(matrix[0])

        # Initialize the transposed matrix
        transposed = [[0] * rows for _ in range(cols)]

        # Iterate through the matrix and transpose the matrix
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

        return transposed


# Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]], Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert Solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Input: [[1, 2, 3], [4, 5, 6]], Output: [[1, 4], [2, 5], [3, 6]]
assert Solution.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

print("All unit tests are passed.")

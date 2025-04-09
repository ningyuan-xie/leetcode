"""566. Reshape the Matrix
Link: https://leetcode.com/problems/reshape-the-matrix/
Difficulty: Easy
Description: In MATLAB, there is a handy function called reshape which can reshape an m x n matrix
into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and
the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same
row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix."""

from typing import List


class Solution:
    @staticmethod
    def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """Optimal Solution: Linear Scan. Time Complexity: O(m * n), Space Complexity: O(m * n).
           Linear Scan: Iterate exactly once through the original matrix"""
        # Get the number of rows and columns of the original matrix
        m, n = len(mat), len(mat[0])  # E.g. [[1, 2], [3, 4]] -> m = 2, n = 2
        # If the reshape operation is not possible, return the original matrix
        if m * n != r * c:
            return mat

        # Initialize the reshaped matrix
        reshaped_mat = [[0] * c for _ in range(r)]  # r x c matrix
        # Linear Scan: Fill the reshaped matrix with the elements of the original matrix
        for i in range(m):
            for j in range(n):
                # Compute the row and column indices of the reshaped matrix
                k = i * n + j  # k is the index of the element in the original matrix
                row, col = divmod(k, c)  # division and modulo returns the tuple (k // c, k % c)
                reshaped_mat[row][col] = mat[i][j]
        return reshaped_mat


# Unit Test: Input: mat = [[1, 2], [3, 4]], r = 1, c = 4, Output: [[1, 2, 3, 4]]
assert Solution.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]

# Unit Test: Input: mat = [[1, 2], [3, 4]], r = 2, c = 4, Output: [[1, 2], [3, 4]]
assert Solution.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]

# Unit Test: Input: mat = [[1, 2], [3, 4]], r = 4, c = 1, Output: [[1], [2], [3], [4]]
assert Solution.matrixReshape([[1, 2], [3, 4]], 4, 1) == [[1], [2], [3], [4]]

print("All unit tests are passed")

"""566. Reshape the Matrix
Link: https://leetcode.com/problems/reshape-the-matrix/
Difficulty: Easy
Description: In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix."""

from typing import List


class Solution:
    @staticmethod
    def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """Optimal Solution: Linear Scan. Time Complexity: O(m*n), Space Complexity: O(m*n)."""
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
            
        # Flatten the matrix into 1D array
        elements = [num for row in mat for num in row]
        
        # Reshape into r x c matrix
        reshaped_matrix = []
        for i in range(r):
            start_idx, end_idx = i * c, (i + 1) * c
            row = elements[start_idx:end_idx]
            reshaped_matrix.append(row)
        return reshaped_matrix


def unit_tests():
    # Input: mat = [[1, 2], [3, 4]], r = 1, c = 4, Output: [[1, 2, 3, 4]]
    assert Solution.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]

    # Input: mat = [[1, 2], [3, 4]], r = 2, c = 4, Output: [[1, 2], [3, 4]]
    assert Solution.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]

    # Input: mat = [[1, 2], [3, 4]], r = 4, c = 1, Output: [[1], [2], [3], [4]]
    assert Solution.matrixReshape([[1, 2], [3, 4]], 4, 1) == [[1], [2], [3], [4]]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

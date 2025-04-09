"""2033. Modify the Matrix
Link: https://leetcode.com/problems/modify-the-matrix/
Difficulty: Easy
Description: Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix
called answer. Make answer equal to matrix, then replace each element with the value -1
with the maximum element in its respective column.
Return the matrix answer."""

from typing import List


class Solution:
    @staticmethod
    def modifiedMatrix(matrix: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: Matrix Manipulation.
           Time Complexity: O(mn), Space Complexity: O(1)"""
        # Get the number of rows and columns
        row, col = len(matrix), len(matrix[0])

        # Get the maximum element in each column
        max_cols = [max([matrix[i][j] for i in range(row)]) for j in range(col)]

        # Replace the elements with -1 with the maximum element in its respective column
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_cols[j]

        return matrix


# Unit Test: matrix = [[1,2,-1],[4,-1,6],[7,8,9]], Output: [[1,2,9],[4,8,6],[7,8,9]]
assert (Solution.modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]])
        == [[1, 2, 9], [4, 8, 6], [7, 8, 9]])

# Unit Test: matrix = [[3,-1],[5,2]], Output: [[3,2],[5,2]]
assert (Solution.modifiedMatrix([[3, -1], [5, 2]]) == [[3, 2], [5, 2]])

print("All unit tests are passed.")

"""1886. Determine Whether Matrix Can Be Obtained By Rotation
Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
Difficulty: Easy
Description: Given two n x n binary matrices mat and target, return true if it is possible to make
mat equal to target by rotating mat in 90-degree increments, or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
        """Optimal Solution: Matrix Rotation & List Comprehension.
           Time Complexity: O(n^2), Space Complexity: O(1)."""

        def rotate(matrix: List[List[int]]) -> List[List[int]]:
            """Helper function to rotate a matrix by 90 degrees clockwise.
               E.g. [[1, 2], [3, 4]] -> [[3, 1], [4, 2]]"""
            # Step 1: Transpose the matrix: [[1, 2], [3, 4]] -> [[1, 3], [2, 4]].
            # - Outer loop i: iterate matrix columns, and generate rows for transposed;
            # - Inner loop j: iterate matrix rows, and append to the transposed rows (generate cols)
            transposed = [[matrix[j][i]
                           for j in range(len(matrix))]
                          for i in range(len(matrix[0]))]

            # Step 2: Reverse each row: [[1, 3], [2, 4]] -> [[3, 1], [4, 2]]
            rotated = [row[::-1] for row in transposed]

            return rotated

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False


# Unit Test: mat = [[0, 1], [1, 0]], target = [[1, 0], [0, 1]], Output: True
assert Solution.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]) is True

# Unit Test: mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]], Output: False
assert Solution.findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]) is False

print("All unit tests are passed.")

"""1572. Matrix Diagonal Sum
Link: https://leetcode.com/problems/matrix-diagonal-sum/
Difficulty: Easy
Description: Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary
diagonal that are not part of the primary diagonal."""

from typing import List


class Solution:
    @staticmethod
    def diagonalSum(mat: List[List[int]]) -> int:
        """Optimal Solution: Matrix Traversal. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the sum of the diagonals
        diagonal_sum = 0

        # Iterate through the matrix and sum the primary and secondary diagonals
        for i in range(len(mat)):
            diagonal_sum += mat[i][i]  # Primary diagonal
            diagonal_sum += mat[i][len(mat) - i - 1]  # Secondary diagonal

        # If the matrix has an odd number of rows, subtract the center element from the sum
        if len(mat) % 2:
            diagonal_sum -= mat[len(mat) // 2][len(mat) // 2]

        return diagonal_sum


# Input: mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], Output: 25
assert Solution.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25

# Input: mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], Output: 8
assert Solution.diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8

# Input: mat = [[5]], Output: 5
assert Solution.diagonalSum([[5]]) == 5

print("All unit tests are passed.")

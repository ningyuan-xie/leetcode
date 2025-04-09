"""766. Toeplitz Matrix
Link: https://leetcode.com/problems/toeplitz-matrix/
Difficulty: Easy
Description: Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements."""

from typing import List


class Solution:
    @staticmethod
    def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(m*n), Space Complexity: O(m+n)"""
        # Initialize the dictionary to store the elements of each diagonal
        diagonals = {}

        # Check each element in the matrix
        for i in range(len(matrix)):  # 0, 1, 2
            for j in range(len(matrix[0])):  # 0, 1, 2, 3
                # Diagonal index = row - column: 0 - 0 = 1 - 1 = 2 - 2
                diagonal_index = i - j

                # If the diagonal index is not in the dictionary, add it
                if diagonal_index not in diagonals:
                    diagonals[diagonal_index] = matrix[i][j]
                # If the element is not the same as the previous element in the diagonal, return False
                elif diagonals[diagonal_index] != matrix[i][j]:
                    return False

        return True


# Unit Test: Input: matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], Output: True
assert Solution.is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]) is True

# Unit Test: Input: matrix = [[1, 2], [2, 2]], Output: False
assert Solution.is_toeplitz_matrix([[1, 2], [2, 2]]) is False

# Unit Test: Input: matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [1, 9, 5, 1]], Output: True
assert Solution.is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [1, 9, 5, 1]]) is True

print("All unit tests are passed")

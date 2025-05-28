"""766. Toeplitz Matrix
Link: https://leetcode.com/problems/toeplitz-matrix/
Difficulty: Easy
Description: Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements."""

from typing import List


class Solution:
    @staticmethod
    def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
        """Optimal Solution: Matrix Manipulation. Time Complexity: O(m*n), Space Complexity: O(1)."""
        # Check each element starting from the second row and second column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # Compare current element with the element diagonally above-left
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        
        return True


def unit_tests():
    # Input: matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], Output: True
    assert Solution.is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]) is True

    # Input: matrix = [[1, 2], [2, 2]], Output: False
    assert Solution.is_toeplitz_matrix([[1, 2], [2, 2]]) is False

    # Input: matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [1, 9, 5, 1]], Output: True
    assert Solution.is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [1, 9, 5, 1]]) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""2133. Check if Every Row and Column Contains All Numbers
Link: https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers
Difficulty: Easy
Description: An n x n matrix is valid if every row and every column contains all the integers
from 1 to n (inclusive).
Given an n x n integer matrix matrix, return true if the matrix is valid.
Otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def checkValid(matrix: List[List[int]]) -> bool:
        """Optimal Solution: Matrix Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(matrix)
        # Check if every row and column contains all the integers from 1 to n
        for i in range(n):
            row = set(matrix[i])
            col = set(matrix[j][i] for j in range(n))
            if row != set(range(1, n + 1)) or col != set(range(1, n + 1)):
                return False
        return True


# Unit Test: matrix = [[1,2,3],[3,1,2],[2,3,1]], Output: True
assert Solution.checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]) is True

# Unit Test: matrix = matrix = [[1,1,1],[1,2,3],[1,2,3]], Output: False
assert Solution.checkValid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]) is False

print("All unit tests are passed.")

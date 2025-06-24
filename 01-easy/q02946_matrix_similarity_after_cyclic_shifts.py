"""2946. Matrix Similarity After Cyclic Shifts
Link: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts
Difficulty: Easy
Description: You are given an m x n integer matrix mat and an integer k. The matrix rows are
0-indexed.
The following proccess happens k times:
- Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
- Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
Return true if the final modified matrix after k steps is identical to the original matrix,
and false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def areSimilar(mat: List[List[int]], k: int) -> bool:
        """Optimal Solution: Matrix Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        rows, cols = len(mat), len(mat[0])

        # Iterate through each element in the matrix
        for i in range(rows):
            for j in range(cols):
                if i % 2 == 0:
                    # Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left
                    if mat[i][(j + k) % cols] != mat[i][j]:
                        return False
                elif i % 2 == 1:
                    # Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right
                    if mat[i][j] != mat[i][(j + cols - k) % cols]:
                        return False

        return True


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4, Output: False
assert Solution.areSimilar([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4) is False

# Input: mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2, Output: True
assert Solution.areSimilar([[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2) is True

# Input: mat = [[2,2],[2,2]], k = 3, Output: True
assert Solution.areSimilar([[2, 2], [2, 2]], 3) is True

print("All unit tests are passed.")

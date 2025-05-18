"""1252. Cells with Odd Values in a Matrix
Link: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
Difficulty: Easy
Description: There is an m x n matrix that is initialized to all 0's. There is also a 2D array
indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment
operations on the matrix.
For each location indices[i], do both of the following:
Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the
increment to all locations in indices."""

from typing import List


class Solution:
    @staticmethod
    def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
        """Optimal Solution: Counters for Rows and Columns.
           Time Complexity: O(m * n), Space Complexity: O(m + n)."""
        # Initialize counters to keep track of how many times each row/column has been incremented
        row_counts = [0] * m  # E.g. m = 2: [0, 0]
        col_counts = [0] * n  # E.g. n = 3: [0, 0, 0]

        # Increment counts based on indices
        for (ri, ci) in indices:  # E.g. indices = [[0, 1], [1, 1]]
            # row 0 was incremented once, row 1 was incremented once
            row_counts[ri] += 1  # [0, 0] -> [1, 0] -> [1, 1]
            # col 1 was incremented twice
            col_counts[ci] += 1  # [0, 0, 0] -> [0, 1, 0] -> [0, 2, 0]

        # Odd number of increments will make the value odd
        odd_count = 0
        for i in range(m):
            for j in range(n):
                # Check if the sum of increments is odd
                if (row_counts[i] + col_counts[j]) % 2 == 1:
                    odd_count += 1

        return odd_count


# Unit Test: m = 2, n = 3, indices = [[0, 1], [1, 1]], Output: 6
assert Solution.oddCells(2, 3, [[0, 1], [1, 1]]) == 6

# Unit Test: m = 2, n = 2, indices = [[1, 1], [0, 0]], Output: 0
assert Solution.oddCells(2, 2, [[1, 1], [0, 0]]) == 0

print("All unit tests are passed.")

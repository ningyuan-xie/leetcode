"""1030. Matrix Cells in Distance Order
Link: https://leetcode.com/problems/matrix-cells-in-distance-order/
Difficulty: Easy
Description: You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols
matrix and you are on the cell with the coordinates (rCenter, cCenter).
Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter)
from the smallest distance to the largest distance.
You may return the answer in any order that satisfies this condition.
The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|."""

from typing import List


class Solution:
    @staticmethod
    def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        """Optimal Solution: Sorting with lambda function.
           Time Complexity: O(rows * cols), Space Complexity: O(rows * cols)."""
        # Initialize the result list
        result = []

        # Iterate through the matrix
        for r in range(rows):
            for c in range(cols):
                # Append to the result list: [r, c, Manhattan distance]
                result.append([r, c, abs(r - rCenter) + abs(c - cCenter)])

        # Sort the result list by Manhattan distance; key=lambda x: x[2] sort by the third element
        result.sort(key=lambda x: x[2])

        # Return the result list with only the cell coordinates
        return [[r, c] for r, c, _ in result]


# Unit Test: rows = 1, cols = 2, rCenter = 0, cCenter = 0, Output: [[0, 0], [0, 1]]
# Matrix: [[0, 0], [0, 1]], Center: [0, 0]
assert Solution.allCellsDistOrder(1, 2, 0, 0) == [[0, 0], [0, 1]]

# Unit Test: rows = 2, cols = 2, rCenter = 0, cCenter = 1, Output: [[0, 1], [0, 0], [1, 1], [1, 0]]
# Matrix: [[0, 0], [0, 1],
#          [1, 0], [1, 1]], Center: [0, 1]
assert (Solution.allCellsDistOrder(2, 2, 0, 1)
        == [[0, 1], [0, 0], [1, 1], [1, 0]])

# Unit Test: rows = 2, cols = 3, rCenter = 1, cCenter = 2,
# Output: [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
# Matrix: [[0, 0], [0, 1], [0, 2],
#          [1, 0], [1, 1], [1, 2]], Center: [1, 2]
assert (Solution.allCellsDistOrder(2, 3, 1, 2)
        == [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]])

print("All unit tests are passed.")

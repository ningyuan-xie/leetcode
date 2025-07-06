"""1351. Count Negative Numbers in a Sorted Matrix
Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
Difficulty: Easy
Description: Given a m x n matrix grid which is sorted in non-increasing order both row-wise and
column-wise, return the number of negative numbers in grid."""

from typing import List


class Solution:
    @staticmethod
    def countNegatives(grid: List[List[int]]) -> int:
        """Optimal Solution: Start from the bottom-left corner of the matrix.
           Time Complexity: O(m+n), Space Complexity: O(1)."""
        # Initialize the number of negative numbers to 0
        count = 0

        # Start from the bottom-left corner of the matrix
        row, col = len(grid) - 1, 0

        # Traverse the matrix from the bottom-left corner
        while row >= 0 and col < len(grid[0]):
            # If the current element is negative, all the elements to the right are also negative
            if grid[row][col] < 0:
                count += len(grid[0]) - col
                # Current row is done, move to the row above
                row -= 1
            # If the current element is non-negative, some elements to the right can still be negative
            else:
                col += 1

        return count


# Input: grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], Output: 8
assert (Solution.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
        == 8)

# Input: grid = [[3, 2], [1, 0]], Output: 0
assert Solution.countNegatives([[3, 2], [1, 0]]) == 0

# Input: grid = [[1, -1], [-1, -1]], Output: 3
assert Solution.countNegatives([[1, -1], [-1, -1]]) == 3

# Input: grid = [[-1]], Output: 1
assert Solution.countNegatives([[-1]]) == 1

print("All unit tests are passed.")

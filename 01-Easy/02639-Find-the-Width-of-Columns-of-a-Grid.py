"""2639. Find the Width of Columns of a Grid
Link: https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/
Difficulty: Easy
Description: You are given a 0-indexed m x n integer matrix grid. The width of a column is the
maximum length of its integers.
- For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
Return an integer array ans of size n where ans[i] is the width of the ith column.
The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise."""

from typing import List


class Solution:
    @staticmethod
    def findColumnWidth(grid: List[List[int]]) -> List[int]:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize variables to track the number of rows and columns
        rows = len(grid)
        cols = len(grid[0])
        result = [0] * cols

        # Iterate through each column
        for i in range(cols):
            # Iterate through each row in the current column
            for j in range(rows):
                # Update the maximum width for the current column
                result[i] = max(result[i], len(str(grid[j][i])))

        return result


# Unit Test: grid = [[1],[22],[333]], Output: [3]
assert Solution.findColumnWidth([[1], [22], [333]]) == [3]

# Unit Test: grid = [[-15,1,3],[15,7,12],[5,6,-2]], Output: [3,1,2]
assert Solution.findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]) == [3, 1, 2]

print("All unit tests are passed.")

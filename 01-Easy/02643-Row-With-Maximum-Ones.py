"""2643. Row With Maximum Ones
Link: https://leetcode.com/problems/row-with-maximum-ones/
Difficulty: Easy
Description: Given a m x n binary matrix mat, find the 0-indexed position of the row that contains
the maximum count of ones, and the number of ones in that row.
In case there are multiple rows that have the maximum count of ones, the row with the smallest row
number should be selected.
Return an array containing the index of the row, and the number of ones in it."""

from typing import List


class Solution:
    @staticmethod
    def rowAndMaximumOnes(mat: List[List[int]]) -> List[int]:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize variables to track the number of rows and columns
        rows = len(mat)
        cols = len(mat[0])
        max_ones = 0
        max_row = 0

        # Iterate through each row
        for i in range(rows):
            # Initialize variables to track the count of ones in the current row
            count_ones = 0
            for j in range(cols):
                if mat[i][j] == 1:
                    count_ones += 1

            # Update the maximum number of ones and the corresponding row
            if count_ones > max_ones:
                max_ones = count_ones
                max_row = i

        return [max_row, max_ones]


# Unit Test: mat = [[0,1],[1,0]], Output: [0, 1]
assert Solution.rowAndMaximumOnes([[0, 1], [1, 0]]) == [0, 1]

# Unit Test: mat = [[0,0,0],[0,1,1]], Output: [1, 2]
assert Solution.rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]) == [1, 2]

# Unit Test: mat = [[0,0],[1,1],[0,0]], Output: [1, 2]
assert Solution.rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]) == [1, 2]

# Unit Test: mat = [[0],[0]], Output: [0, 0]
assert Solution.rowAndMaximumOnes([[0], [0]]) == [0, 0]

print("All unit tests are passed.")

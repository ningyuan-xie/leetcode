"""118. Pascal's Triangle
Link: https://leetcode.com/problems/pascals-triangle/
Difficulty: Easy
Description: Given an integer numRows, return the first numRows of Pascal's triangle."""

from typing import List


class Solution:
    @staticmethod
    def generate(numRows: int) -> List[List[int]]:
        """Optimal Solution: Iteration.
           Time Complexity: O(numRows^2), Space Complexity: O(numRows^2)."""
        # Initialize the result list with the first row of Pascal's triangle
        result = [[1]]
        # Generate the subsequent (numRows - 1) rows of Pascal's triangle
        for i in range(numRows - 1):  # -1 because we already have the first row
            temp_row = [0] + result[-1] + [0]  # E.g. [1] -> [0, 1, 0]
            current_row = []
            # Current row's length = previous row's length + 1
            for j in range(len(result[-1]) + 1):  # E.g. [1]'s next row length is 2
                current_row.append(temp_row[j] + temp_row[j + 1])  # E.g. [0 + 1, 1 + 0] = [1, 1]
            # Append the current row to the result list
            result.append(current_row)
        return result


# Input: numRows = 5, Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert Solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Input: numRows = 1, Output: [[1]]
assert Solution.generate(1) == [[1]]

# Input: numRows = 2, Output: [[1],[1,1]]
assert Solution.generate(2) == [[1], [1, 1]]

print("All unit tests are passed.")

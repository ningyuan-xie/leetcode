"""119. Pascal's Triangle II
Link: https://leetcode.com/problems/pascals-triangle-ii/
Difficulty: Easy
Description: Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle."""

from typing import List


class Solution:
    @staticmethod
    def getRow(rowIndex: int) -> List[int]:
        """Optimal Solution: Iteration. Time complexity: O(n^2), Space complexity: O(n)"""
        # Initialize the result list with the first row of Pascal's triangle
        result = [[1]]
        # Generate the subsequent (numRows - 1) rows of Pascal's triangle
        for i in range(rowIndex):  # rowIndex = numRows - 1
            temp_row = [0] + result[-1] + [0]
            current_row = []
            # Current row's length = previous row's length + 1
            for j in range(len(result[-1]) + 1):  # E.g. [1]'s next row length is 2
                current_row.append(temp_row[j] + temp_row[j + 1])  # E.g. [0 + 1, 1 + 0] = [1, 1]
            # Append the current row to the result list
            result.append(current_row)
        return result[-1]


# Input: rowIndex = 3, Output: [1,3,3,1]
assert Solution.getRow(3) == [1, 3, 3, 1]

# Input: rowIndex = 0, Output: [1]
assert Solution.getRow(0) == [1]

# Input: rowIndex = 1, Output: [1,1]
assert Solution.getRow(1) == [1, 1]

print("All unit tests are passed.")

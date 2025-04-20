"""119. Pascal's Triangle II
Link: https://leetcode.com/problems/pascals-triangle-ii/
Difficulty: Easy
Description: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown."""

from typing import List


class Solution:
    @staticmethod
    def getRow(rowIndex: int) -> List[int]:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(n)."""
        # Initialize the result list with the first row of Pascal's triangle
        result = [1]

        # Generate the subsequent (rowIndex) rows of Pascal's triangle
        for i in range(rowIndex):
            # Create a new row with 1 at the beginning and end
            current_row = [1] * (len(result) + 1)
            # Fill in the values of the current row based on the previous row
            for j in range(1, len(current_row) - 1):
                current_row[j] = result[j - 1] + result[j]
            # Update the result list to the current row
            result = current_row

        return result


def unit_tests():
    # Input: rowIndex = 3, Output: [1,3,3,1]
    assert Solution.getRow(3) == [1, 3, 3, 1]

    # Input: rowIndex = 0, Output: [1]
    assert Solution.getRow(0) == [1]

    # Input: rowIndex = 1, Output: [1,1]
    assert Solution.getRow(1) == [1, 1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

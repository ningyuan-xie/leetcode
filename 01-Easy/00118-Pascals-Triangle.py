"""118. Pascal's Triangle
Link: https://leetcode.com/problems/pascals-triangle/
Difficulty: Easy
Description: Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown."""

from typing import List


class Solution:
    @staticmethod
    def generate(numRows: int) -> List[List[int]]:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(n)."""
        # Initialize the result list with the first row of Pascal's triangle
        result = [[1]]

        # Generate the subsequent (numRows - 1) rows of Pascal's triangle
        for i in range(numRows - 1):
            # Create a new row with 1 at the beginning and end
            current_row = [1] * (len(result[-1]) + 1)
            # Fill in the values of the current row based on the previous row
            for j in range(1, len(current_row) - 1):
                current_row[j] = result[-1][j - 1] + result[-1][j]
            # Append the current row to the result list
            result.append(current_row)
        
        return result


def unit_tests():
    # Input: numRows = 5, Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert Solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    # Input: numRows = 1, Output: [[1]]
    assert Solution.generate(1) == [[1]]

    # Input: numRows = 2, Output: [[1],[1,1]]
    assert Solution.generate(2) == [[1], [1, 1]]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

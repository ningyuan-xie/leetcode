"""3127. Make a Square with the Same Color
Link: https://leetcode.com/problems/make-a-square-with-the-same-color
Difficulty: Easy
Description: You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and
'W'. Character 'W' represents the white color, and character 'B' represents the black color.
Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where
all cells are of the same color.
Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def canMakeSquare(grid: List[List[str]]) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(1), Space Complexity: O(1)"""
        rows, cols = len(grid), len(grid[0])

        def isSquareOfSameColor(r, c):
            """Helper function to check if a 2x2 square is of the same color"""
            count_white, count_black = 0, 0
            for i in range(r, r + 2):
                for j in range(c, c + 2):
                    if grid[i][j] == 'W':
                        count_white += 1
                    else:
                        count_black += 1
            return count_white == 4 or count_black == 4 or count_white == 3 or count_black == 3

        # Check if there is a 2x2 square of the same color
        for row in range(rows - 1):
            for col in range(cols - 1):
                if isSquareOfSameColor(row, col):
                    return True
        return False


# Unit Test: grid = [["B","W","B"],["B","W","W"],["B","W","B"]], Output = True
assert Solution.canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]) is True

# Unit Test: grid = [["B","W","B"],["W","B","W"],["B","W","B"]], Output = False
assert Solution.canMakeSquare([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]) is False

# Unit Test: grid = [["B","W","B"],["B","W","W"],["B","W","W"]], Output = True
assert Solution.canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]) is True

print("All unit tests are passed")

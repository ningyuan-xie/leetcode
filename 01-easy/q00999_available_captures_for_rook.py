"""999. Available Captures for Rook
Link: https://leetcode.com/problems/available-captures-for-rook/
Difficulty: Easy
Description: You are given an 8 x 8 matrix representing a chessboard. There is exactly one white
rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'.
Empty squares are represented by '.'.
A rook can move any number of squares horizontally or vertically (up, down, left, right) until it
reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the
pawn's square in one move.
Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot
attack a pawn if there is another piece blocking the path.
Return the number of pawns the white rook is attacking."""

from typing import List


class Solution:
    @staticmethod
    def numRookCaptures(board: List[List[str]]) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(1), Space Complexity: O(1)."""
        # Find the rook's position on the board:
        # next() returns the first element that satisfies the condition
        rook_row, rook_col = next((i, j) for i in range(8) for j in range(8) if board[i][j] == 'R')

        # Initialize the number of captures
        captures = 0
        # Check the four directions from the rook's position
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        for (dx, dy) in directions:
            # Move to the next square in the direction by 1 step
            x, y = rook_row + dx, rook_col + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p':
                    captures += 1
                    break
                if board[x][y] == 'B':
                    break
                # Move to the next square in the direction by 1 step
                x, y = x + dx, y + dy

        return captures


# Unit Test: rook is at (2, 3); the rook is attacking all the pawns
board_test = [[".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", "R", ".", ".", ".", "p"],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."]]
assert Solution.numRookCaptures(board_test) == 3

# Unit Test: rook is at (3, 3); the rook is attacking all the pawns
board_test = [[".", ".", ".", ".", ".", ".", ".", "."],
              [".", "p", "p", "p", "p", "p", ".", "."],
              [".", "p", "p", "B", "p", "p", ".", "."],
              [".", "p", "B", "R", "B", "p", ".", "."],
              [".", "p", "p", "B", "p", "p", ".", "."],
              [".", "p", "p", "p", "p", "p", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."]]
assert Solution.numRookCaptures(board_test) == 0

# Unit Test: rook is at (3, 3); the rook is attacking the pawns at positions b5, d6, and f5
board_test = [[".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."],
              ["p", "p", ".", "R", ".", "p", "B", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", "B", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."]]
assert Solution.numRookCaptures(board_test) == 3

print("All unit tests are passed.")

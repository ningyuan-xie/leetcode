"""1275. Find Winner on a Tic Tac Toe Game
Link: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
Difficulty: Easy
Description: Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
• Players take turns placing characters into empty squares ' '.
• The first player A always places 'X' characters, while the second player B always places 'O' characters.
• 'X' and 'O' characters are always placed into empty squares, never on filled ones.
• The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
• The game also ends if all squares are non-empty.
• No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first."""

from typing import List


class Solution:
    @staticmethod
    def tictactoe(moves: List[List[int]]) -> str:
        """Optimal Solution: Simulation. Time Complexity: O(1), Space Complexity: O(1)."""
        # Initialize the board
        board = [[''] * 3 for _ in range(3)]  # [['', '', ''], ['', '', ''], ['', '', '']]

        # Fill the board with the moves
        for i, (r, c) in enumerate(moves):
            board[r][c] = 'A' if i % 2 == 0 else 'B'

        # Check the rows and columns
        for i in range(3):
            # Check the rows
            if board[i][0] == board[i][1] == board[i][2] != '':
                return board[i][0]

            # Check the columns
            if board[0][i] == board[1][i] == board[2][i] != '':
                return board[0][i]

        # Check the main diagonal
        if board[0][0] == board[1][1] == board[2][2] != '':
            return board[0][0]

        # Check the anti-diagonal
        if board[0][2] == board[1][1] == board[2][0] != '':
            return board[0][2]

        # Check if there are still moves left
        if len(moves) < 9:
            return "Pending"

        # If no winner and no moves left, it's a draw
        return "Draw"


def unit_tests():
    # Input: moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], Output: "A"
    assert Solution.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]) == "A"

    # Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], Output: "B"
    assert Solution.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]) == "B"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

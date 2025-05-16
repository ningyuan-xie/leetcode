"""657. Robot Return to Origin
Link: https://leetcode.com/problems/robot-return-to-origin/
Difficulty: Easy
Description: There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move."""


class Solution:
    @staticmethod
    def judgeCircle(moves: str) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        x = y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return x == 0 and y == 0


def unit_test():
    # Input: moves = "UD", Output: True
    assert Solution.judgeCircle("UD") is True

    # Input: moves = "LL", Output: False
    assert Solution.judgeCircle("LL") is False

    # Input: moves = "UDLR", Output: True
    assert Solution.judgeCircle("UDLR") is True


if __name__ == "__main__":
    unit_test()
    print("All unit tests are passed.")

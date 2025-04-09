"""657. Robot Return to Origin
Link: https://leetcode.com/problems/robot-return-to-origin/
Difficulty: Easy
Description: There is a robot starting at the position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves."""


class Solution:
    @staticmethod
    def judgeCircle(moves: str) -> bool:
        """Optimal Solution: Count the number of moves.
           Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the counts of the four moves
        up = down = left = right = 0

        # Count the number of 'U', 'D', 'L', and 'R' moves
        for move in moves:
            if move == 'U':
                up += 1
            elif move == 'D':
                down += 1
            elif move == 'L':
                left += 1
            elif move == 'R':
                right += 1

        # Check if the robot returns to the origin
        return up == down and left == right


# Unit Test: Input: moves = "UD", Output: True
assert Solution.judgeCircle("UD") is True

# Unit Test: Input: moves = "LL", Output: False
assert Solution.judgeCircle("LL") is False

# Unit Test: Input: moves = "UDLR", Output: True
assert Solution.judgeCircle("UDLR") is True

print("All unit tests are passed")

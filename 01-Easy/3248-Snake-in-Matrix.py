"""3248. Snake in Matrix
Link: https://leetcode.com/problems/snake-in-matrix
Difficulty: Easy
Description: There is a snake in an n x n matrix grid and can move in four possible directions.
Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.
The snake starts at cell 0 and follows a sequence of commands.
You are given an integer n representing the size of the grid and an array of strings commands
where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT". It's guaranteed that the
snake will remain within the grid boundaries throughout its movement.
Return the position of the final cell where the snake ends up after executing commands."""

from typing import List


class Solution:
    @staticmethod
    def finalPositionOfSnake(n: int, commands: List[str]) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(m), Space Complexity: O(n^2)"""
        # Initialize the matrix
        matrix = [[(i * n) + j for j in range(n)] for i in range(n)]

        x = commands.count("DOWN") - commands.count("UP")
        y = commands.count("RIGHT") - commands.count("LEFT")

        return matrix[x][y]


# Unit Test: n = 2, commands = ["RIGHT","DOWN"], Output: 3
assert Solution.finalPositionOfSnake(2, ["RIGHT", "DOWN"]) == 3

# Unit Test: n = 3, commands = ["DOWN","RIGHT","UP"], Output: 1
assert Solution.finalPositionOfSnake(3, ["DOWN", "RIGHT", "UP"]) == 1

print("All unit tests are passed")

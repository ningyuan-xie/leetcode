"""2660. Determine the Winner of a Bowling Game
Link: https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
Difficulty: Easy
Description: You are given two 0-indexed integer arrays player1 and player2, representing the
number of pins that player 1 and player 2 hit in a bowling game, respectively.
The bowling game consists of n turns, and the number of pins in each turn is exactly 10.
Assume a player hits xi pins in the ith turn. The value of the ith turn for the player is:
- 2xi if the player hits 10 pins in either (i - 1)th or (i - 2)th turn.
- Otherwise, it is xi.
The score of the player is the sum of the values of their n turns.
Return
- 1 if the score of player 1 is more than the score of player 2,
- 2 if the score of player 2 is more than the score of player 1, and
- 0 in case of a draw."""

from typing import List


class Solution:
    @staticmethod
    def isWinner(player1: List[int], player2: List[int]) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize variables to track the number of turns and the scores of the players
        turns = len(player1)
        score1, score2 = 0, 0

        # Iterate through each turn
        for i in range(turns):
            # Initialize variables to track the value of the current turn for each player
            value1 = player1[i]
            value2 = player2[i]

            # Check if the player hits 10 pins in the previous two turns
            if i == 1:
                if player1[i - 1] == 10:
                    value1 *= 2
                if player2[i - 1] == 10:
                    value2 *= 2

            elif i >= 2:
                if player1[i - 1] == 10 or player1[i - 2] == 10:
                    value1 *= 2
                if player2[i - 1] == 10 or player2[i - 2] == 10:
                    value2 *= 2

            # Update the scores of the players
            score1 += value1
            score2 += value2

        # Return the result based on the scores of the players
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0


# Input: player1 = [5,10,3,2], player2 = [6,5,7,3], Output: 1
assert Solution.isWinner([5, 10, 3, 2], [6, 5, 7, 3]) == 1

# Input: player1 = [3,5,7,6], player2 = [8,10,10,2], Output: 2
assert Solution.isWinner([3, 5, 7, 6], [8, 10, 10, 2]) == 2

# Input: player1 = [2,3], player2 = [4,1], Output: 2
assert Solution.isWinner([2, 3], [4, 1]) == 0

# Input: player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1],
# Output: 2
assert Solution.isWinner([1, 1, 1, 10, 10, 10, 10],
                         [10, 10, 10, 10, 1, 1, 1]) == 2

print("All unit tests are passed.")

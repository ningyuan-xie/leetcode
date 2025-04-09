"""3238. Find the Number of Winning Players
Link: https://leetcode.com/problems/find-the-number-of-winning-players
Difficulty: Easy
Description: You are given an integer n representing the number of players in a game and a 2D
array pick where pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.
Player i wins the game if they pick strictly more than i balls of the same color. In other words,
- Player 0 wins if they pick any ball.
- Player 1 wins if they pick at least two balls of the same color.
- ...
- Player i wins if they pick at least i + 1 balls of the same color.
Return the number of players who win the game.
Note that multiple players can win the game."""

from typing import List


class Solution:
    @staticmethod
    def winningPlayerCount(n: int, pick: List[List[int]]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize a dictionary to count the number of balls picked by each player
        player_count = {i: {} for i in range(n)}

        # Count the number of balls picked by each player
        for x, y in pick:
            player_count[x][y] = player_count[x].get(y, 0) + 1
        # E.g. {0: {0: 1}, 1: {0: 2}, 2: {1: 2, 0: 1}, 3: {}}

        # Count the number of players who win the game
        winning_players = 0
        for player_index in range(n):
            for color, count in player_count[player_index].items():
                if count > player_index:
                    winning_players += 1
                    break

        return winning_players


# Unit Test: n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]], Output: 2
assert Solution.winningPlayerCount(4, [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]) == 2

# Unit Test: n = 5, pick = [[1,1],[1,2],[1,3],[1,4]], Output: 0
assert Solution.winningPlayerCount(5, [[1, 1], [1, 2], [1, 3], [1, 4]]) == 0

# Unit Test: n = 5, pick = [[1,1],[2,4],[2,4],[2,4]], Output: 1
assert Solution.winningPlayerCount(5, [[1, 1], [2, 4], [2, 4], [2, 4]]) == 1

print("All unit tests are passed.")

"""3222. Find the Winning Player in Coin Game
Link: https://leetcode.com/problems/find-the-winning-player-in-coin-game
Difficulty: Easy
Description: You are given two positive integers x and y, denoting the number of coins with
values 75 and 10 respectively.
Alice and Bob are playing a game. Each turn, starting with Alice, the player must pick up coins
with a total value 115. If the player is unable to do so, they lose the game.
Return the name of the player who wins the game if both players play optimally."""


class Solution:
    @staticmethod
    def winningPlayer(x: int, y: int) -> str:
        """Optimal Solution: Greedy Approach. Time Complexity: O(1), Space Complexity: O(1)"""
        # Each player has to pick 1 coin of 75 and 4 coins of 10 to make 115
        turn_x = x // 1
        turn_y = y // 4
        turn = min(turn_x, turn_y)  # The number of turns both players can play optimally

        # If the number of turns is even, Bob wins, else Alice wins
        return "Alice" if turn % 2 == 1 else "Bob"


# Unit Test: x = 2, y = 7, Output: "Alice"
assert Solution.winningPlayer(2, 7) == "Alice"

# Unit Test: x = 4, y = 11, Output: "Bob"
assert Solution.winningPlayer(4, 11) == "Bob"

print("All unit tests are passed.")

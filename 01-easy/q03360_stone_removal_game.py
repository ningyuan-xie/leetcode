"""3360. Stone Removal Game
Link: https://leetcode.com/problems/stone-removal-game/
Difficulty: Easy
Description: Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
Alice starts by removing exactly 10 stones on her first turn.
For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
The player who cannot make a move loses the game.
Given a positive integer n, return true if Alice wins the game and false otherwise."""


class Solution:
    def canAliceWin(n: int) -> bool:
        """Optimal Solution: While Simulation. Time Complexity: O(1), Space Complexity: O(1)."""
        move = 10
        turn = 0  # 0 for Alice, 1 for Bob

        while n >= move:
            n -= move
            move -= 1
            turn ^= 1  # Flip turn

        # Alice wins if it's Bob's turn now
        return turn == 1


def unit_tests():
    # Input: n = 12, Output: true
    assert Solution.canAliceWin(12) is True

    # Input: n = 1, Output: false
    assert Solution.canAliceWin(1) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

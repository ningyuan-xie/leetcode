"""1025. Divisor Game
Link: https://leetcode.com/problems/divisor-game/
Difficulty: Easy
Description: Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
• Choosing any x with 0 < x < n and n % x == 0.
• Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally."""


class Solution:
    @staticmethod
    def divisorGame(n: int) -> bool:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        # Alice always wins if n is even
        return n % 2 == 0


def unit_tests():
    # Input: n = 2, Output: True
    assert Solution.divisorGame(2) is True

    # Input: n = 3, Output: False
    assert Solution.divisorGame(3) is False

    # Input: n = 4, Output: True
    assert Solution.divisorGame(4) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

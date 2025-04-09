"""292. Nim Game
Link: https://leetcode.com/problems/nim-game/
Difficulty: Easy
Description: You are playing the following Nim Game with your friend:
Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner."""


class Solution:
    @staticmethod
    def canWinNim(n: int) -> bool:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)
        The player who removes the last stone wins the game.
        The player who removes the stone(s) such that the remaining stones are multiples of 4 wins.
        The player will win as long as the remaining stones are not multiples of 4"""
        return n % 4 != 0


# Input: n = 4, Output: False
assert Solution.canWinNim(4) is False

# Input: n = 1, Output: True
assert Solution.canWinNim(1) is True

# Input: n = 2, Output: True
assert Solution.canWinNim(2) is True

# Input: n = 7, Output: True
assert Solution.canWinNim(7) is True  # The player can remove 3 stones, so the remaining stones are 4

print("All unit tests are passed.")

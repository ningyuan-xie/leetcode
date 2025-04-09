"""2027. Minimum Moves to Convert String
Link: https://leetcode.com/problems/minimum-moves-to-convert-string
Difficulty: Easy
Description: You are given a string s consisting of n characters which are either 'X' or 'O'.
A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note
that if a move is applied to the character 'O', it will stay the same.
Return the minimum number of moves required so that all the characters of s are converted to 'O'."""

from typing import List


class Solution:
    @staticmethod
    def minimumMoves(s: str) -> int:
        """Optimal Solution: Greedy Approach. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the number of moves required to convert the string
        moves = 0
        # Initialize the index to traverse the string
        i = 0

        while i < len(s):
            # Check if the current character is 'X'
            if s[i] == 'X':
                # Increment the number of moves
                moves += 1
                # Greedy: Skip the next 2 characters and move to the 4th character
                i += 3
            else:
                # Move to the next character
                i += 1

        return moves


# Unit Test: s = "XXX", Output: 1
assert Solution.minimumMoves("XXX") == 1

# Unit Test: s = "XXOX", Output: 2
assert Solution.minimumMoves("XXOX") == 2

# Unit Test: s = "OOOO", Output: 0
assert Solution.minimumMoves("OOOO") == 0

print("All unit tests are passed")

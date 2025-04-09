"""3274. Check if Two Chessboard Squares Have the Same Color
Link: https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/
Difficulty: Easy
Description: You are given two strings, coordinate1 and coordinate2, representing the coordinates 
of a square on an 8 x 8 chessboard.
Return true if these two squares have the same color and false otherwise.
The coordinate will always represent a valid chessboard square. The coordinate will always 
have the letter first (indicating its column), and the number second (indicating its row)."""


class Solution:
    @staticmethod
    def checkTwoChessboards(coordinate1: str, coordinate2: str) -> bool: 
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        # Convert the column letter to a number (1-8)
        col1 = ord(coordinate1[0]) - ord('a') + 1
        col2 = ord(coordinate2[0]) - ord('a') + 1

        # Convert the row number to an integer
        row1 = int(coordinate1[1])
        row2 = int(coordinate2[1])

        # Check if both squares have the same color by comparing the parity of their coordinates
        return (col1 + row1) % 2 == (col2 + row2) % 2

        
# Unit Test: coordinate1 = "a1", coordinate2 = "c3", Output: True
assert Solution.checkTwoChessboards("a1", "c3") is True

# Unit Test: coordinate1 = "a1", coordinate2 = "h3", Output: False
assert Solution.checkTwoChessboards("a1", "h3") is False

print("All unit tests are passed.")

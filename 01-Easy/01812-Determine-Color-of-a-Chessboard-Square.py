"""1812. Determine Color of a Chessboard Square
Link: https://leetcode.com/problems/determine-color-of-a-chessboard-square/
Difficulty: Easy
Description: You are given coordinates, a string that represents the coordinates of a square of the
chessboard.
Below is a chessboard for your reference.
Return true if the square is white, and false if the square is black.
The coordinate will always represent a valid chessboard square. The coordinate will always have the
letter first, and the number second."""


class Solution:
    @staticmethod
    def square_is_white(coordinates: str) -> bool:
        """Optimal Solution: Check Coordinates. Time Complexity: O(1), Space Complexity: O(1)"""
        # Convert column to a numeric value ('a' -> 1, 'b' -> 2, ..., 'h' -> 8)
        col = ord(coordinates[0]) - ord('a') + 1
        # Convert row to an integer
        row = int(coordinates[1])

        # E.g. 'h3' -> (8, 3) -> (8 + 3) % 2 == 1 -> True
        return (col + row) % 2 == 1


# Unit Test: coordinates = "a1", Output: False
assert Solution.square_is_white("a1") is False

# Unit Test: coordinates = "h3", Output: True
assert Solution.square_is_white("h3") is True

# Unit Test: coordinates = "c7", Output: False
assert Solution.square_is_white("c7") is False

print("All unit tests are passed")

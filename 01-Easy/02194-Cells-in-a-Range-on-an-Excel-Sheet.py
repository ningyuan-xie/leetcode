"""2194. Cells in a Range on an Excel Sheet
Link: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
Difficulty: Easy
Description: A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
- <col> denotes the column number c of the cell. It is represented by alphabetical letters.
-- For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
- <row> is the row number r of the cell. The rth row is represented by the integer r.
You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the
column c1, <row1> represents the row r1, <col2> represents the column c2, and <row2> represents
the row r2, such that r1 <= r2 and c1 <= c2.
Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be
represented as strings in the format mentioned above and be sorted in non-decreasing order first
by columns and then by rows."""

from typing import List


class Solution:
    @staticmethod
    def cellsInRange(s: str) -> List[str]:
        """Optimal Solution: chr() and ord() functions.
           Time Complexity: O(n), Space Complexity: O(1)"""
        # Parse the range string
        start_col, start_row, end_col, end_row = s[0], s[1], s[3], s[4]

        # Generate all cells in the range
        return [
            f"{chr(c)}{r}"
            for c in range(ord(start_col), ord(end_col) + 1)  # chr(ord('A')) = 'A'
            for r in range(int(start_row), int(end_row) + 1)
        ]


# Unit Test: s = "K1:L2", Output: ["K1", "K2", "L1", "L2"]
assert Solution.cellsInRange("K1:L2") == ["K1", "K2", "L1", "L2"]

# Unit Test: s = "A1:F1", Output: ["A1", "B1", "C1", "D1", "E1", "F1"]
assert Solution.cellsInRange("A1:F1") == ["A1", "B1", "C1", "D1", "E1", "F1"]

print("All unit tests are passed.")

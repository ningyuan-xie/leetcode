"""171. Excel Sheet Column Number
Link: https://leetcode.com/problems/excel-sheet-column-number/
Difficulty: Easy
Description: Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number."""


class Solution:
    @staticmethod
    def titleToNumber(columnTitle: str) -> int:
        """Optimal Solution: Math. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the result variable
        result = 0

        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)

        return result


def unit_tests():
    # Input: columnTitle = "A", Output: 1
    assert Solution.titleToNumber("A") == 1

    # Input: columnTitle = "AB", Output: 28
    assert Solution.titleToNumber("AB") == 28

    # Input: columnTitle = "ZY", Output: 701
    assert Solution.titleToNumber("ZY") == 701

    # Input: columnTitle = "FXSHRXW", Output: 2147483647
    assert Solution.titleToNumber("FXSHRXW") == 2147483647


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

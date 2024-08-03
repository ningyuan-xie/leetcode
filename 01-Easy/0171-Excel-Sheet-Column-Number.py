"""171. Excel Sheet Column Number
Link: https://leetcode.com/problems/excel-sheet-column-number/
Difficulty: Easy
Description: Given a string columnTitle that represents the column title
as it appears in an Excel sheet, return its corresponding column number."""


class Solution:
    @staticmethod
    def titleToNumber(columnTitle: str) -> int:
        """Optimal Solution: Math. Time Complexity: O(n), Space Complexity: O(1)
           Reverse of 0168-Excel-Sheet-Column-Title.py"""
        # Initialize the column number
        column_number = 0
        # Traverse the column title from LEFT to RIGHT
        for char in columnTitle:  # "AB": 'A' -> 'B'
            # Multiply the current column number by 26 to move to the next letter on the right
            # '' -> 'A' -> 'AB'
            column_number *= 26
            # Add the value of the current character to the column number
            column_number += ord(char) - ord('A')  # ord('A') = 65, ord('B') = 66
            # Add 1 to the column number to make it 1-indexed
            column_number += 1
        return column_number


# Unit Test: Input: columnTitle = "A", Output: 1
assert Solution.titleToNumber("A") == 1

# Unit Test: Input: columnTitle = "AB", Output: 28
assert Solution.titleToNumber("AB") == 28

# Unit Test: Input: columnTitle = "ZY", Output: 701
assert Solution.titleToNumber("ZY") == 701

# Unit Test: Input: columnTitle = "FXSHRXW", Output: 2147483647
assert Solution.titleToNumber("FXSHRXW") == 2147483647

print("All unit tests are passed")

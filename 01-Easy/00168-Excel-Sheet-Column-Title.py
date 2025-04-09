"""168. Excel Sheet Column Title
Link: https://leetcode.com/problems/excel-sheet-column-title/
Difficulty: Easy
Description: Given an integer columnNumber,
return its corresponding column title as it appears in an Excel sheet."""


class Solution:
    @staticmethod
    def convertToTitle(columnNumber: int) -> str:
        """Optimal Solution: Math. Time Complexity: O(log(columnNumber)), Space Complexity: O(1).
           Similar to 0067-Add-Binary.py"""
        result = ""
        # Title will be filled from RIGHT to LEFT
        while columnNumber > 0:
            # Subtract 1 from columnNumber to make it 0-indexed for each digit
            columnNumber -= 1
            remainder = columnNumber % 26
            # 65 is the ASCII value of 'A': chr(65) = 'A', chr(66) = 'B', ..., chr(90) = 'Z'
            # Add char to the front of the string: 'B' -> 'A' + 'B' = 'AB'
            result = chr(remainder + ord('A')) + result
            # Divide columnNumber by 26 using floor division to move to the next digit on the left
            columnNumber //= 26
        return result


# Input: columnNumber = 1, Output: "A"
assert Solution.convertToTitle(1) == "A"

# Input: columnNumber = 28, Output: "AB"
assert Solution.convertToTitle(28) == "AB"

# Input: columnNumber = 701, Output: "ZY"
assert Solution.convertToTitle(701) == "ZY"

# Input: columnNumber = 2147483647, Output: "FXSHRXW"
assert Solution.convertToTitle(2147483647) == "FXSHRXW"

print("All unit tests are passed.")

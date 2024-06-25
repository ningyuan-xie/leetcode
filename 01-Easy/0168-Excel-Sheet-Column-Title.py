# Link: https://leetcode.com/problems/excel-sheet-column-title/
# Difficulty: Easy
# Description: Given an integer columnNumber,
# return its corresponding column title as it appears in an Excel sheet.


class Solution:
    @staticmethod
    def convertToTitle(columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            # Subtract 1 from columnNumber to make it 0-indexed for each digit
            columnNumber -= 1
            # Append the character corresponding to the remainder of columnNumber divided by 26
            # 65 is the ASCII value of 'A': chr(65) = 'A', chr(66) = 'B', ..., chr(90) = 'Z'
            result = chr(columnNumber % 26 + 65) + result  # Append char to the left: 'A' + 'B' = 'AB'
            # Divide columnNumber by 26 using floor division "//" to get the next digit
            columnNumber //= 26
        return result


# Unit Test: Input: columnNumber = 1, Output: "A"
assert Solution.convertToTitle(1) == "A"

# Unit Test: Input: columnNumber = 28, Output: "AB"
assert Solution.convertToTitle(28) == "AB"

# Unit Test: Input: columnNumber = 701, Output: "ZY"
assert Solution.convertToTitle(701) == "ZY"

# Unit Test: Input: columnNumber = 2147483647, Output: "FXSHRXW"
assert Solution.convertToTitle(2147483647) == "FXSHRXW"

print("All unit tests are passed")

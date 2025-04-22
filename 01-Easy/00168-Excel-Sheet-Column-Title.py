"""168. Excel Sheet Column Title
Link: https://leetcode.com/problems/excel-sheet-column-title/
Difficulty: Easy
Description: Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet."""


class Solution:
    @staticmethod
    def convertToTitle(columnNumber: int) -> str:
        """Optimal Solution: Math. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        # Initialize an empty string to store the result
        result = ""

        while columnNumber > 0:
            # Decrement columnNumber by 1 to handle 1-based indexing
            columnNumber -= 1

            # Calculate the current character and prepend it to the result
            result = chr(columnNumber % 26 + ord('A')) + result

            # Update columnNumber for the next iteration
            columnNumber //= 26

        return result


def unit_tests():
    # Input: columnNumber = 1, Output: "A"
    assert Solution.convertToTitle(1) == "A"

    # Input: columnNumber = 28, Output: "AB"
    assert Solution.convertToTitle(28) == "AB"

    # Input: columnNumber = 701, Output: "ZY"
    assert Solution.convertToTitle(701) == "ZY"

    # Input: columnNumber = 2147483647, Output: "FXSHRXW"
    assert Solution.convertToTitle(2147483647) == "FXSHRXW"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

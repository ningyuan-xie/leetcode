"""1556. Thousand Separator
Link: https://leetcode.com/problems/thousand-separator/
Difficulty: Easy
Description: Given an integer n, add a dot (".") as the thousands separator and return it in string
format."""


class Solution:
    @staticmethod
    def thousandSeparator(n: int) -> str:
        """Optimal Solution: Reverse Iteration. Time Complexity: O(n), Space Complexity: O(1)"""
        # Convert the integer to a string
        n_str = str(abs(n))  # Handle the absolute value to ignore negative sign for now

        # Initialize the result string
        result = ""

        # Iterate through the string in reverse order
        for i in range(len(n_str) - 1, -1, -1):
            # When the length of the result is 3, 7, 11, ... (3 + 4 * k), add a dot
            if len(result) % 4 == 3:
                result = "." + result  # "9" -> "89" -> "789" -> ".789" -> ... -> "456.789"

            result = n_str[i] + result  # Add the current character to the front of the result

        # Add back the negative sign if the original number was negative
        if n < 0:
            result = "-" + result

        return result


# Unit Test: n = 987, Output: "987"
assert Solution.thousandSeparator(987) == "987"

# Unit Test: n = 1234, Output: "1.234"
assert Solution.thousandSeparator(1234) == "1.234"

# Unit Test: n = 123456789, Output: "123.456.789"
assert Solution.thousandSeparator(123456789) == "123.456.789"

print("All unit tests are passed.")

"""2259. Remove Digit From Number to Maximize Result
Link: https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
Difficulty: Easy
Description: You are given a string number representing a positive integer and a character digit.
Return the resulting string after removing exactly one occurrence of digit from number such that
the value of the resulting string in decimal form is maximized. The test cases are generated such
that digit occurs at least once in number."""


class Solution:
    @staticmethod
    def removeDigit(number: str, digit: str) -> str:
        """Optimal Solution: Iterate Through Each Character.
           Time Complexity: O(n), Space Complexity: O(n)."""
        max_result = ""

        # Iterate through each character in the number
        for i in range(len(number)):
            if number[i] == digit:
                # Create a new number by removing the digit at index i
                new_number = number[:i] + number[i + 1:]

                # Update the maximum result if the new number is larger
                if new_number > max_result:
                    max_result = new_number

        return max_result


# Input: number = "123", digit = "3", Output: "12"
assert Solution.removeDigit("123", "3") == "12"

# Input: number = "1231", digit = "1", Output: "231"
assert Solution.removeDigit("1231", "1") == "231"

# Input: number = "551", digit = "5", Output: "51"
assert Solution.removeDigit("551", "5") == "51"

# Input: number = "939", digit = "9", Output: "93"
assert Solution.removeDigit("939", "9") == "93"

print("All unit tests are passed.")

"""2710. Remove Trailing Zeros From a String
Link: https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
Difficulty: Easy
Description: Given a positive integer num represented as a string, return the integer num without
trailing zeros as a string."""


class Solution:
    @staticmethod
    def removeTrailingZeros(num: str) -> str:
        """Optimal Solution: Reverse Traversal. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the index to track the last non-zero character
        index = len(num) - 1

        # Continue the loop until the index is greater than or equal to 0
        while index >= 0:
            # If the character is not zero
            if num[index] != "0":
                break
            # Move the index
            index -= 1

        # Return the string without trailing zeros
        return num[:index + 1]


# Unit Test: num = "51230100", Output: "512301"
assert Solution.removeTrailingZeros("51230100") == "512301"

# Unit Test: num = "123", Output: "123"
assert Solution.removeTrailingZeros("123") == "123"

print("All unit tests are passed.")

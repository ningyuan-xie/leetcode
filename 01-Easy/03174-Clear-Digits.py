"""3174. Clear Digits
Link: https://leetcode.com/problems/clear-digits
Difficulty: Easy
Description: You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
- Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
Note that the operation cannot be performed on a digit that does not have any non-digit character
to its left."""


class Solution:
    @staticmethod
    def clearDigits(s: str) -> str:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize a stack to keep track of characters
        stack = []

        # Iterate through the string
        for char in s:
            # If the character is a digit
            if char.isdigit():
                # Pop the last character from the stack
                stack.pop()
            # If the character is not a digit
            else:
                # Add the character to the stack
                stack.append(char)

        # Return the final result
        return "".join(stack)


# Unit Test: s = "abc", Output = "abc"
assert Solution.clearDigits("abc") == "abc"

# Unit Test: s = "cb34", Output = ""
assert Solution.clearDigits("cb34") == ""

print("All unit tests are passed")

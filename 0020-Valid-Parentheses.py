# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        # Create dictionary with key-value pairs
        bracket_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        # Initialize stack
        stack = []
        # Loop through input string
        for char in s:
            # If the character is an opening bracket, add it to the stack
            if char in bracket_dict:  # E.g. "(", "{", "["
                stack.append(char)
            # If the character is a closing bracket, check if the stack is empty
            # or the last element in the stack is not the corresponding opening bracket
            # If so, return False
            elif not stack or bracket_dict[stack.pop()] != char:
                return False
        # If the stack is empty, return True
        return not stack


# Unit Test: Input: s = "()", Output: True
assert Solution.isValid("()") == True

# Unit Test: Input: s = "()[]{}", Output: True
assert Solution.isValid("()[]{}") == True

# Unit Test: Input: s = "(]", Output: False
assert Solution.isValid("(]") == False
print("All unit tests are passed")

"""20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid."""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)"""
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
            # Otherwise, pop from the non-empty stack (if empty, cannot pop, return False)
            # if the last element is not the corresponding opening bracket, return False
            elif not stack or bracket_dict[stack.pop()] != char:
                return False
        # If the stack has popped all the elements, return True
        return True if not stack else False


# Unit Test: Input: s = "()", Output: True
assert Solution.isValid("()") == True

# Unit Test: Input: s = "()[]{}", Output: True
assert Solution.isValid("()[]{}") == True

# Unit Test: Input: s = "(]", Output: False
assert Solution.isValid("(]") == False

# Unit Test: Input: s = "]", Output: False
assert Solution.isValid("]") == False

print("All unit tests are passed")

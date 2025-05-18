"""20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type."""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)."""
        # Dictionary to hold the mapping of closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop from stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # Return True if stack is empty (all brackets matched), otherwise False
        return not stack


def unit_tests():
    # Input: s = "()", Output: True
    assert Solution.isValid("()") is True

    # Input: s = "()[]{}", Output: True
    assert Solution.isValid("()[]{}") is True

    # Input: s = "(]", Output: False
    assert Solution.isValid("(]") is False

    # Input: s = "]", Output: False
    assert Solution.isValid("]") is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""1021. Remove Outermost Parentheses
Link: https://leetcode.com/problems/remove-outermost-parentheses/
Difficulty: Easy
Description: A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
• For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s."""


class Solution:
    @staticmethod
    def removeOuterParentheses(s: str) -> str:
        """Optimal Solution: Count the number of open parentheses. Time Complexity: O(n), Space Complexity: O(n)."""
        # Track the level of parentheses
        open_count, result = 0, []

        # Iterate through the string
        for char in s:
            if char == "(":
                # Only add the parenthesis if it's not an outermost one
                if open_count > 0:
                    result.append(char)
                # Increase the count of open parentheses
                open_count += 1
            elif char == ")":
                # Decrease the count of open parentheses
                open_count -= 1
                # Only add the parenthesis if it's not an outermost one
                if open_count > 0:
                    result.append(char)

        # Return the string without outermost parentheses
        return "".join(result)


def unit_tests():
    # Input: s = "(()())(())", Output: "()()()"
    assert Solution.removeOuterParentheses("(()())(())") == "()()()"

    # Input: s = "(()())(())(()(()))", Output: "()()()()(())"
    assert Solution.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"

    # Input: s = "()()", Output: ""
    assert Solution.removeOuterParentheses("()()") == ""


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

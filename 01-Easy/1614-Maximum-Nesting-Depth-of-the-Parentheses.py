"""1614. Maximum Nesting Depth of the Parentheses
Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
Difficulty: Easy
Description: Given a valid parentheses string s, return the nesting depth of s.
The nesting depth is the maximum number of nested parentheses."""


class Solution:
    @staticmethod
    def maxDepth(s: str) -> int:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the maximum depth and current depth
        max_depth, current_depth = 0, 0

        # Iterate through each character in the string
        for char in s:
            # Greedy Approach: update max_depth whenever current_depth increases
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        return max_depth


# Unit Test: s = "(1+(2*3)+((8)/4))+1", Output: 3
assert Solution.maxDepth("(1+(2*3)+((8)/4))+1") == 3

# Unit Test: s = "(1)+((2))+(((3)))", Output: 3
assert Solution.maxDepth("(1)+((2))+(((3)))") == 3

# Unit Test: s = "1+(2*3)/(2-1)", Output: 1
assert Solution.maxDepth("1+(2*3)/(2-1)") == 1

# Unit Test: s = "1", Output: 0
assert Solution.maxDepth("1") == 0

print("All unit tests are passed")

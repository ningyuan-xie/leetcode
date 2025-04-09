"""1047. Remove All Adjacent Duplicates In String
Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Difficulty: Easy
Description: You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique."""


class Solution:
    @staticmethod
    def removeDuplicates(s: str) -> str:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the stack
        stack = []

        # Iterate through the string
        for char in s:
            # If the stack is not empty and the top of the stack is equal to the current character
            if stack and stack[-1] == char:
                stack.pop()  # Remove the top of the stack
            else:
                stack.append(char)  # Add the current character to the stack

        # Return the final string by joining the stack
        return "".join(stack)


# Unit Test: s = "abbaca", Output: "ca"
assert Solution.removeDuplicates("abbaca") == "ca"

# Unit Test: s = "azxxzy", Output: "ay"
assert Solution.removeDuplicates("azxxzy") == "ay"

# Unit Test: s = "a", Output: "a"
assert Solution.removeDuplicates("a") == "a"

print("All unit tests are passed.")

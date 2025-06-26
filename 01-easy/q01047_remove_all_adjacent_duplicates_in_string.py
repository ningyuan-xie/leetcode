"""1047. Remove All Adjacent Duplicates In String
Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Difficulty: Easy
Description: You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique."""


class Solution:
    @staticmethod
    def removeDuplicates(s: str) -> str:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)."""
        stack = []

        for char in s:
            # If the stack is not empty and the top of the stack is equal to the current character
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        # Return the final string by joining the stack
        return "".join(stack)


def unit_tests():
    # Input: s = "abbaca", Output: "ca"
    assert Solution.removeDuplicates("abbaca") == "ca"

    # Input: s = "azxxzy", Output: "ay"
    assert Solution.removeDuplicates("azxxzy") == "ay"

    # Input: s = "a", Output: "a"
    assert Solution.removeDuplicates("a") == "a"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

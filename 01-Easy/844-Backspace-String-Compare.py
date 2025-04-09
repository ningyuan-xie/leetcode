"""844. Backspace String Compare
Link: https://leetcode.com/problems/backspace-string-compare/
Difficulty: Easy
Description: Given two strings s and t, return true if they are equal when both are typed into
empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty."""


class Solution:
    @staticmethod
    def backspaceCompare(s: str, t: str) -> bool:
        """Optimal Solution: Reverse Iteration. Time Complexity: O(n), Space Complexity: O(n)"""

        def process_string(string: str) -> str:
            """Helper function to process the string"""
            result, skip = [], 0
            for char in reversed(string):
                # If the character is '#', then increment the skip counter
                if char == '#':
                    skip += 1
                # If there are characters to skip, skip them and decrement the skip counter
                elif skip > 0:
                    skip -= 1
                # Otherwise, add the character to the result
                else:
                    result.append(char)
            return ''.join(result)

        return process_string(s) == process_string(t)


# Unit Test: Input: s = "ab#c", t = "ad#c", Output: True
assert Solution.backspaceCompare("ab#c", "ad#c") is True

# Unit Test: Input: s = "ab##", t = "c#d#", Output: True
assert Solution.backspaceCompare("ab##", "c#d#") is True

# Unit Test: Input: s = "a##c", t = "#a#c", Output: True
assert Solution.backspaceCompare("a##c", "#a#c") is True

# Unit Test: Input: s = "a#c", t = "b", Output: False
assert Solution.backspaceCompare("a#c", "b") is False

print("All unit tests are passed")

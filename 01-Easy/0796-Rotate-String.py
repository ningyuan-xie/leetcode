"""796. Rotate String
Link: https://leetcode.com/problems/rotate-string/
Difficulty: Easy
Description: Given two strings s and goal, return true if and only if s can become goal after
some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift."""


class Solution:
    @staticmethod
    def rotateString(s: str, goal: str) -> bool:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)"""
        return len(s) == len(goal) and goal in s + s


# Unit Test: Input: s = 'abcde', goal = 'cdeab', Output: True
assert Solution.rotateString('abcde', 'cdeab') is True

# Unit Test: Input: s = 'abcde', goal = 'abced', Output: False
assert Solution.rotateString('abcde', 'abced') is False

# Unit Test: Input: s = 'abcde', goal = 'abcde', Output: True
assert Solution.rotateString('abcde', 'abcde') is True

# Unit Test: Input: s = 'abcde', goal = 'abcdeabcde', Output: False
assert Solution.rotateString('abcde', 'abcdeabcde') is False

print("All unit tests are passed")

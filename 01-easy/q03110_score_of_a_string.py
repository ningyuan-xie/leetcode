"""3110. Score of a String
Link: https://leetcode.com/problems/score-of-a-string
Difficulty: Easy
Description: You are given a string s. The score of a string is defined as the sum of the
absolute difference between the ASCII values of adjacent characters.
Return the score of s."""


class Solution:
    @staticmethod
    def scoreOfString(s: str) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        score = 0

        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))

        return score


# Unit Test: s = "hello", Output = 13
assert Solution.scoreOfString("hello") == 13

# Unit Test: s = "zaz", Output = 50
assert Solution.scoreOfString("zaz") == 50

print("All unit tests are passed.")

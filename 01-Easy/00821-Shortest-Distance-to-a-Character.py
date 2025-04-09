"""821. Shortest Distance to a Character
Link: https://leetcode.com/problems/shortest-distance-to-a-character/
Difficulty: Easy
Description: Given a string s and a character c that occurs in s, return an array of integers
answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to
the character c in s."""

from typing import List


class Solution:
    @staticmethod
    def shortestToChar(s: str, c: str) -> List[int]:
        """Optimal Solution: Two Passes. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the result array
        n = len(s)
        result = [0] * n

        # Initialize the last occurrence of the character as negative infinity
        last_occurrence_index = float('-inf')
        # Pass 1: Forward pass: Calculate the shortest distance to the left
        for i in range(n):
            if s[i] == c:
                last_occurrence_index = i
            result[i] = i - last_occurrence_index
        # E.g. s = "loveleetcode", c = "e" -> [inf, inf, inf, 0, 1, 0, 0, 1, 2, 3, 4, 0]

        # Initialize the last occurrence of the character as positive infinity
        last_occurrence_index = float('inf')
        # Pass 2: Backward pass: Calculate the shortest distance to the right
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_occurrence_index = i
            result[i] = min(result[i], last_occurrence_index - i)
        # E.g. s = "loveleetcode", c = "e" -> [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

        return result


# Input: s = "loveleetcode", c = "e", Output: [3,2,1,0,1,0,0,1,2,2,1,0]
assert Solution.shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

# Input: s = "aaab", c = "b", Output: [3,2,1,0]
assert Solution.shortestToChar("aaab", "b") == [3, 2, 1, 0]

# Input: s = "aaba", c = "b", Output: [2,1,0,1]
assert Solution.shortestToChar("aaba", "b") == [2, 1, 0, 1]

print("All unit tests are passed.")

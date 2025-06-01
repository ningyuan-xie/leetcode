"""821. Shortest Distance to a Character
Link: https://leetcode.com/problems/shortest-distance-to-a-character/
Difficulty: Easy
Description: Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
The distance between two indices i and j is abs(i - j), where abs is the absolute value function."""

from typing import List


class Solution:
    @staticmethod
    def shortestToChar(s: str, c: str) -> List[int]:
        """Optimal Solution: Two Passes. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(s)
        result = [0] * n
        
        # Forward pass: left to right
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev
        
        # Backward pass: right to left
        prev = float('inf')
        for i in range(n-1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)
        
        return result


def unit_tests():
    # Input: s = "loveleetcode", c = "e", Output: [3,2,1,0,1,0,0,1,2,2,1,0]
    assert Solution.shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

    # Input: s = "aaab", c = "b", Output: [3,2,1,0]
    assert Solution.shortestToChar("aaab", "b") == [3, 2, 1, 0]

    # Input: s = "aaba", c = "b", Output: [2,1,0,1]
    assert Solution.shortestToChar("aaba", "b") == [2, 1, 0, 1]


if __name__ == '__main__':
    unit_tests()
    print("All unit tests are passed.")

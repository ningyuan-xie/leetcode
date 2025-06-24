"""1967. Number of Strings That Appear as Substrings in Word
Link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
Difficulty: Easy
Description: Given an array of strings patterns and a string word, return the number of strings
in patterns that exist as a substring in word.
A substring is a contiguous sequence of characters within a string."""

from typing import List


class Solution:
    @staticmethod
    def numOfStrings(patterns: List[str], word: str) -> int:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        count = 0

        for pattern in patterns:
            if pattern in word:
                count += 1

        return count


# Input: patterns = ["a", "abc", "bc", "d"], word = "abc", Output: 3
assert Solution.numOfStrings(["a", "abc", "bc", "d"], "abc") == 3

# Input: patterns = ["a", "b", "c"], word = "aaaa", Output: 1
assert Solution.numOfStrings(["a", "b", "c"], "aaaa") == 1

# Input: patterns = ["a", "a", "a"], word = "ab", Output: 3
assert Solution.numOfStrings(["a", "a", "a"], "ab") == 3

print("All unit tests are passed.")

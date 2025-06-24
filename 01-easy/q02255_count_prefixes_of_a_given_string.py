"""2255. Count Prefixes of a Given String
Link: https://leetcode.com/problems/count-prefixes-of-a-given-string/
Difficulty: Easy
Description: You are given a string array words and a string s, where words[i] and s comprise
only of lowercase English letters.
Return the number of strings in words that are a prefix of s.
A prefix of a string is a substring that occurs at the beginning of the string. A substring is a
contiguous sequence of characters within a string."""

from typing import List


class Solution:
    @staticmethod
    def countPrefixes(words: List[str], s: str) -> int:
        """Optimal Solution: .startswith(). Time Complexity: O(n), Space Complexity: O(1).
           Same as 2185. Counting Words With a Given Prefix"""
        count = 0
        for word in words:
            if s.startswith(word):
                count += 1
        return count


# Input: words = ["a","b","c","ab","bc","abc"], s = "abc", Output: 3
assert Solution.countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc") == 3

# Input: words = ["a","a"], s = "aa", Output: 2
assert Solution.countPrefixes(["a", "a"], "aa") == 2

print("All unit tests are passed.")

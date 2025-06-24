"""2828. Check if a String Is an Acronym of Words
Link: https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/
Difficulty: Easy
Description: Given an array of strings words and a string s, determine if s is an acronym of words.
The string s is considered an acronym of words if it can be formed by concatenating the first
character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"],
but it can't be formed from ["bear", "aardvark"].
Return true if s is an acronym of words, and false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def isAcronym(words: List[str], s: str) -> bool:
        """Optimal Solution: String Concatenation. Time Complexity: O(n), Space Complexity: O(1)."""
        return s == ''.join([word[0] for word in words])


# Input: words = ["alice","bob","charlie"], s = "abc", Output: True
assert Solution.isAcronym(["alice", "bob", "charlie"], "abc") is True

# Input: words = ["an","apple"], s = "a", Output: False
assert Solution.isAcronym(["an", "apple"], "a") is False

# Input: words = ["never","gonna","give","up","on","you"], s = "ngguoy", Output: True
assert Solution.isAcronym(["never", "gonna", "give", "up", "on", "you"], "ngguoy") is True

print("All unit tests are passed.")

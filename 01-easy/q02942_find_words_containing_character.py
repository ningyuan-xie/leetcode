"""2942. Find Words Containing Character
Link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Difficulty: Easy
Description: You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order."""

from typing import List


class Solution:
    @staticmethod
    def findWordsContaining(words: List[str], x: str) -> List[int]:
        """Optimal Solution: String Matching. Time Complexity: O(n), Space Complexity: O(1)."""
        return [i for i, word in enumerate(words) if x in word]


# Input: words = ["leet","code"], x = "e", Output: [0,1]
assert Solution.findWordsContaining(["leet", "code"], "e") == [0, 1]

# Input: words = ["abc","bcd","aaaa","cbc"], x = "a", Output: [0, 2]
assert Solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a") == [0, 2]

# Input: words = ["abc","bcd","aaaa","cbc"], x = "z", Output: []
assert Solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z") == []

print("All unit tests are passed.")

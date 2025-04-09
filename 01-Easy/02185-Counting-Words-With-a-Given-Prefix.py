"""2185. Counting Words With a Given Prefix
Link: https://leetcode.com/problems/counting-words-with-a-given-prefix/
Difficulty: Easy
Description: You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s."""

from typing import List


class Solution:
    @staticmethod
    def countWords(words: List[str], pref: str) -> int:
        """Optimal Solution: .startswith(). Time Complexity: O(n), Space Complexity: O(1)"""
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


# Unit Test: words = ["pay","attention","practice","attend"], prefix = "at", Output: 2
assert Solution.countWords(["pay", "attention", "practice", "attend"], "at") == 2

# Unit Test: words = ["leetcode","win","loops","success"], pref = "code", Output: 0
assert Solution.countWords(["leetcode", "win", "loops", "success"], "code") == 0

print("All unit tests are passed.")

"""1961. Check If String Is a Prefix of Array
Link: https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
Difficulty: Easy
Description: Given a string s and an array of strings words, determine whether s is a prefix string
of words.
A string s is a prefix string of words if s can be made by concatenating the first k strings in
words for some positive k no larger than words.length.
Return true if s is a prefix string of words, or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def isPrefixString(s: str, words: List[str]) -> bool:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the result string
        result = ""

        # Iterate through the words
        for word in words:
            result += word
            if result == s:
                return True

            # Break the loop if the result is longer than s
            if len(result) > len(s):
                break

        return False


# Input: s = "iloveleetcode", words = ["i", "love", "leetcode", "apples"], Output: True
assert Solution.isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"]) is True

# Input: s = "iloveleetcode", words = ["apples", "i", "love", "leetcode"], Output: False
assert Solution.isPrefixString("iloveleetcode", ["apples", "i", "love", "leetcode"]) is False

# Input: s = "a", words = ["a", "aa", "aaa"], Output: True
assert Solution.isPrefixString("a", ["a", "aa", "aaa"]) is True

print("All unit tests are passed.")

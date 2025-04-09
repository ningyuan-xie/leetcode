"""2114. Maximum Number of Words Found in Sentences
Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences
Difficulty: Easy
Description: A sentence is a list of words that are separated by a single space with no leading
or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in a single sentence."""

from typing import List


class Solution:
    @staticmethod
    def mostWordsFound(sentences: List[str]) -> int:
        """Optimal Solution: Splitting by Space. Time Complexity: O(n), Space Complexity: O(1)"""
        return max(len(sentence.split())
                   for sentence in sentences)


# Unit Test: sentences = ["alice and bob love leetcode", "i think so too",
# "this is great thanks very much"], Output: 6
assert Solution.mostWordsFound(["alice and bob love leetcode", "i think so too",
                                "this is great thanks very much"]) == 6

# Unit Test: sentences = ["please wait", "continue to fight", "continue to win"], Output: 3
assert Solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3

print("All unit tests are passed")

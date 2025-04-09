"""884. Uncommon Words from Two Sentences
Link: https://leetcode.com/problems/uncommon-words-from-two-sentences/
Difficulty: Easy
Description: A sentence is a string of single-space separated words where each word consists only
of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the
other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer
in any order."""

from typing import List


class Solution:
    @staticmethod
    def uncommonFromSentences(s1: str, s2: str) -> List[str]:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Combine two sentences into one sentence
        sentences = s1.split() + s2.split()
        # Initialize a hash table to store the frequency of each word
        freq = {}
        for word in sentences:
            freq[word] = freq.get(word, 0) + 1

        # Return the list of uncommon words
        return [word for word in freq if freq[word] == 1]


# Input: A = "this apple is sweet", B = "this apple is sour", Output: ["sweet","sour"]
assert Solution.uncommonFromSentences("this apple is sweet",
                                      "this apple is sour") == ["sweet", "sour"]

# Input: A = "apple apple", B = "banana", Output: ["banana"]
assert Solution.uncommonFromSentences("apple apple", "banana") == ["banana"]

print("All unit tests are passed.")

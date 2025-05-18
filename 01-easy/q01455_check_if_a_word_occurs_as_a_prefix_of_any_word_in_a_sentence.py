"""1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
Link: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
Difficulty: Easy
Description: Given a sentence that consists of some words separated by a single space, and a
searchWord, check if searchWord is a prefix of any word in sentence.
Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word.
If searchWord is a prefix of more than one word, return the index of the first word (minimum index).
If there is no such word return -1.
A prefix of a string s is any leading contiguous substring of s."""

from typing import List


class Solution:
    @staticmethod
    def isPrefixOfWord(sentence: str, searchWord: str) -> int:
        """Optimal Solution: .split() method and .startswith() method.
           Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the word index
        word_index = 1

        # Iterate through the words in the sentence
        for word in sentence.split():
            # If the search word is a prefix of the current word, return the word index
            if word.startswith(searchWord):
                return word_index
            # Otherwise, increment the word index
            word_index += 1

        # If the search word is not a prefix of any word, return -1
        return -1


# Unit Test: sentence = "i love eating burger", searchWord = "burg", Output: 4
assert Solution.isPrefixOfWord("i love eating burger", "burg") == 4

# Unit Test: sentence = "this problem is an easy problem", searchWord = "pro", Output: 2
assert Solution.isPrefixOfWord("this problem is an easy problem", "pro") == 2

# Unit Test: sentence = "i am tired", searchWord = "you", Output: -1
assert Solution.isPrefixOfWord("i am tired", "you") == -1

# Unit Test: sentence = "i use triple pillow", searchWord = "pill", Output: 4
assert Solution.isPrefixOfWord("i use triple pillow", "pill") == 4

# Unit Test: sentence = "hello from the other side", searchWord = "they", Output: -1
assert Solution.isPrefixOfWord("hello from the other side", "they") == -1

print("All unit tests are passed.")

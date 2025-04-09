"""290. Word Pattern
Link: https://leetcode.com/problems/word-pattern/
Difficulty: Easy
Description: Given a pattern and a string s, find if s follows the same pattern."""


class Solution:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 0205-Isomorphic-Strings.py"""
        # Split the string into a list of words
        words = s.split()  # E.g. "dog cat cat dog" -> ["dog", "cat", "cat", "dog"]
        # If the length of the pattern and the number of words are not equal, return False
        if len(pattern) != len(words):
            return False
        # Initialize the hash tables to store the mapping between the pattern and the words
        pattern_to_word = {}
        word_to_pattern = {}
        # Iterate through the pattern and the words
        for char, word in zip(pattern, words):
            # Check if mutual mapping is violated
            if ((char in pattern_to_word and pattern_to_word[char] != word) or
                    (word in word_to_pattern and word_to_pattern[word] != char)):
                return False
            # Update the mapping between the pattern and the word
            pattern_to_word[char] = word  # pattern_to_word: {'a': 'dog', 'b': 'cat'}
            word_to_pattern[word] = char  # word_to_pattern: {'dog': 'a', 'cat': 'b'}
        # If all the mappings are consistent, return True
        return True


# Input: pattern = "abba", s = "dog cat cat dog", Output: True
assert Solution.wordPattern("abba", "dog cat cat dog") is True

# Input: pattern = "abba", s = "dog cat cat fish", Output: False
assert Solution.wordPattern("abba", "dog cat cat fish") is False

# Input: pattern = "aaaa", s = "dog cat cat dog", Output: False
assert Solution.wordPattern("aaaa", "dog cat cat dog") is False

# Input: pattern = "abba", s = "dog dog dog dog", Output: False
assert Solution.wordPattern("abba", "dog dog dog dog") is False

print("All unit tests are passed.")

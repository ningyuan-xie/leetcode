"""290. Word Pattern
Link: https://leetcode.com/problems/word-pattern/
Difficulty: Easy
Description: Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
• Each letter in pattern maps to exactly one unique word in s.
• Each unique word in s maps to exactly one letter in pattern.
• No two letters map to the same word, and no two words map to the same letter."""


class Solution:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Split the string into words
        words = s.split()

        # Check if the length of pattern and words are the same
        if len(pattern) != len(words):
            return False

        # Create two dictionaries to store character to word mapping and word to character mapping
        char_to_word = {}
        word_to_char = {}

        # Iterate through both pattern and words simultaneously
        for char, word in zip(pattern, words):
            # Check if the mapping exists in both dictionaries
            if (char in char_to_word and char_to_word[char] != word or
                    word in word_to_char and word_to_char[word] != char):
                return False

            # Create the mapping if it doesn't exist
            char_to_word[char] = word
            word_to_char[word] = char

        return True


def unit_tests():
    # Input: pattern = "abba", s = "dog cat cat dog", Output: True
    assert Solution.wordPattern("abba", "dog cat cat dog") is True

    # Input: pattern = "abba", s = "dog cat cat fish", Output: False
    assert Solution.wordPattern("abba", "dog cat cat fish") is False

    # Input: pattern = "aaaa", s = "dog cat cat dog", Output: False
    assert Solution.wordPattern("aaaa", "dog cat cat dog") is False

    # Input: pattern = "abba", s = "dog dog dog dog", Output: False
    assert Solution.wordPattern("abba", "dog dog dog dog") is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

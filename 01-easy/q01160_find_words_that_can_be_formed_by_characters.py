"""1160. Find Words That Can Be Formed by Characters
Link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Difficulty: Easy
Description: You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words."""

from typing import List


class Solution:
    @staticmethod
    def countCharacters(words: List[str], chars: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize a dictionary to store the count of characters in chars
        char_count = {}
        for char in chars:
            char_count[char] = char_count.get(char, 0) + 1  # {'a': 2, 't': 1, 'c': 1, 'h': 1}

        # Initialize the total length of good strings
        total_length = 0

        # Iterate through the list of words
        for word in words:
            # Initialize a dictionary to store the count of characters in the word
            word_count = {}

            # Check if the word can be formed by characters from chars
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1  # {'c': 1, 'a': 1, 't': 1}

            # Check if the word is good
            is_good = True
            for char in word_count:  # loop through the keys of word_count
                if char_count.get(char, 0) < word_count[char]:
                    is_good = False
                    break

            # Increment the total length of good strings
            if is_good:
                total_length += len(word)

        return total_length


# Input: words = ["cat", "bt", "hat", "tree"], chars = "atach", Output: 6
assert Solution.countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6

# Input: words = ["hello", "world", "leetcode"], chars = "welldonehoneyr", Output: 10
assert Solution.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr") == 10

# Input: words = ["cat", "bt", "hat", "tree"], chars = "atach", Output: 6
assert Solution.countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6

print("All unit tests are passed.")

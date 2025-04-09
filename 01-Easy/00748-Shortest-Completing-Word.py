"""748. Shortest Completing Word
Link: https://leetcode.com/problems/shortest-completing-word/
Difficulty: Easy
Description: Given a string licensePlate and an array of strings words, find the shortest completing
word in words.
A completing word is a word that contains all the letters in licensePlate. Ignore numbers and
spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in
licensePlate, then it must appear in the word the same number of times or more.
For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case),
and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".
Return the shortest completing word in words. It is guaranteed an answer exists.
If there are multiple shortest completing words, return the first one that occurs in words."""

from typing import List


class Solution:
    @staticmethod
    def shortest_completing_word(licensePlate: str, words: List[str]) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1).
           n is the number of words in the list;
           length of licensePlate and words are considered constant"""
        # Extract the letters and convert to lowercase
        license_letters = [char.lower() for char in licensePlate if char.isalpha()]

        # Count the frequency of each letter in the license plate
        required_counts = {}
        for char in license_letters:
            required_counts[char] = required_counts.get(char, 0) + 1

        # Initialize the shortest word variable
        shortest_word = None

        # Check each word in the list, and count the frequency of each letter
        for word in words:
            word_counts = {}
            for char in word.lower():
                word_counts[char] = word_counts.get(char, 0) + 1

            # Check if the word satisfies the license plate requirements
            if all(word_counts.get(char, 0) >= required_counts[char] for char in required_counts):
                # If this word is shorter or if it's the first word found, update the shortest_word
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word


# Input: license_plate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"],
# Output: "steps"
assert Solution.shortest_completing_word("1s3 PSt",
                                         ["step", "steps", "stripe", "stepple"]) == "steps"

# Input: license_plate = "1s3 456", words = ["looks", "pest", "stew", "show"],
# Output: "pest"
assert Solution.shortest_completing_word("1s3 456",
                                         ["looks", "pest", "stew", "show"]) == "pest"

# Input: license_plate = "Ah71752", words = ["suggest", "letter", "of", "husband", "easy",
# "education", "drug", "prevent", "writer", "old"], Output: "husband"
assert (Solution.shortest_completing_word("Ah71752",
                                          ["suggest", "letter", "of", "husband", "easy",
                                           "education", "drug", "prevent", "writer", "old"])
        == "husband")

print("All unit tests are passed.")

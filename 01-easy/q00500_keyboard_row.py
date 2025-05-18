"""500. Keyboard Row
Link: https://leetcode.com/problems/keyboard-row/
Difficulty: Easy
Description: Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
In the American keyboard:
• the first row consists of the characters "qwertyuiop",
• the second row consists of the characters "asdfghjkl", and
• the third row consists of the characters "zxcvbnm"."""

from typing import List


class Solution:
    @staticmethod
    def findWords(words: List[str]) -> List[str]:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)."""
        # Define the rows of the keyboard as sets for quick lookup
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        # Initialize an empty list to store the result
        result = []

        # Iterate through each word in the input list
        for word in words:
            # Convert the word to lowercase and get the first character's row
            lower_word = word.lower()
            first_char_row = (
                row1 if lower_word[0] in row1 else row2 if lower_word[0] in row2 else row3
            )

            # Check if all characters of the word belong to the same row
            if all(char in first_char_row for char in lower_word):
                result.append(word)

        return result


def unit_tests():
    # Input: words = ["Hello", "Alaska", "Dad", "Peace"], Output: ["Alaska", "Dad"]
    assert Solution.findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]

    # Input: words = ["omk"], Output: []
    assert Solution.findWords(["omk"]) == []

    # Input: words = ["adsdf", "sfd"], Output: ["adsdf", "sfd"]
    assert Solution.findWords(["adsdf", "sfd"]) == ["adsdf", "sfd"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

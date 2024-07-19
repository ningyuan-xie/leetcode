# Link: https://leetcode.com/problems/keyboard-row/
# Difficulty: Easy
# Description: Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.

from typing import List


class Solution:
    # Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def findWords(words: List[str]) -> List[str]:
        # Initialize the keyboard rows
        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        # Initialize the list of words that can be typed using one row
        one_row_words = []
        # Iterate through the input words
        for word in words:
            # Initialize the row of the first letter of the word
            one_row = 0
            # Iterate through the three keyboard rows to determine the one row needed
            for i, keyboard_row in enumerate(keyboard_rows):
                # Use 1st letter of the word to determine the one row needed
                if word[0].lower() in keyboard_row:
                    one_row = i
                    break
            # Check if all the letters of this word are in the same row
            # all() returns True if all elements of the iterable are true
            if all(letter.lower() in keyboard_rows[one_row] for letter in word):
                one_row_words.append(word)
        return one_row_words


# Unit Test: Input: words = ["Hello", "Alaska", "Dad", "Peace"], Output: ["Alaska", "Dad"]
assert Solution.findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]

# Unit Test: Input: words = ["omk"], Output: []
assert Solution.findWords(["omk"]) == []

# Unit Test: Input: words = ["adsdf", "sfd"], Output: ["adsdf", "sfd"]
assert Solution.findWords(["adsdf", "sfd"]) == ["adsdf", "sfd"]

print("All unit tests are passed")

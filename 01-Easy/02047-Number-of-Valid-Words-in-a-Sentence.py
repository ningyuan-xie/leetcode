"""2047. Number of Valid Words in a Sentence
Link: https://leetcode.com/problems/number-of-valid-words-in-a-sentence
Difficulty: Easy
Description: A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens
('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken
down into one or more tokens separated by one or more spaces ' '.
A token is a valid word if all three of the following are true:
- It only contains lowercase letters, hyphens, and/or punctuation (no digits).
- There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters
("a-b" is valid, but "-ab" and "ab-" are not valid).
- There is at most one punctuation mark. If present, it must be at the end of the token
("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
Given a string sentence, return the number of valid words in sentence."""

import re


class Solution:
    @staticmethod
    def countValidWords(sentence: str) -> int:
        """Optimal Solution: Regular Expression. Time Complexity: O(n), Space Complexity: O(n).
           re.fullmatch: Ensures the entire token matches the regex pattern;
           [a-z]*: Matches zero or more lowercase letters at the beginning, such as "penci";
           ([a-z]-[a-z])?: Matches an optional group, with hyphen surrounded by letters, such as "l-s"
           but not "pencil-sharpener", which is why we need [a-z]* at front and end;
           [!.,]?: Matches an optional punctuation mark at the end, such as "." """
        return sum(bool(re.fullmatch(r"[a-z]*([a-z]-[a-z])?[a-z]*[!.,]?", token))
                   for token in sentence.split())


# Unit Test: sentence = "cat and  dog", Output: 3
assert Solution.countValidWords("cat and  dog") == 3

# Unit Test: sentence = "!this  1-s b8d!", Output: 0
assert Solution.countValidWords("!this  1-s b8d!") == 0

# Unit Test: sentence = "alice and  bob are playing stone-game10", Output: 5
assert Solution.countValidWords("alice and  bob are playing stone-game10") == 5

# Unit Test: sentence = ""he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.", Output: 6
assert Solution.countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.") == 6

print("All unit tests are passed")

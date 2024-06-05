# Link: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy
# Description: Given a string s consisting of some words separated by some number of spaces,
# return the length of the last word in the string.

class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        # Split the string by space
        words = s.split()  # E.g. "Hello World" -> ["Hello", "World"]
        # If the list is empty, return 0
        if not words:
            return 0
        # Return the length of the last word
        return len(words[-1])


# Unit Test: Input: s = "Hello World", Output: 5
assert Solution.lengthOfLastWord("Hello World") == 5

# Unit Test: Input: s = "   fly me to   the moon  ", Output: 4
assert Solution.lengthOfLastWord("   fly me to   the moon  ") == 4

# Unit Test: Input: s = "luffy is still joyboy", Output: 6
assert Solution.lengthOfLastWord("luffy is still joyboy") == 6

# Unit Test: Input: s = "a", Output: 1
assert Solution.lengthOfLastWord("a") == 1
print("All unit tests are passed")


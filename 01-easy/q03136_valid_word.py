"""3136. Valid Word
Link: https://leetcode.com/problems/valid-word
Difficulty: Easy
Description: A word is considered valid if:
- It contains a minimum of 3 characters.
- It contains only digits (0-9), and English letters (uppercase and lowercase).
- It includes at least one vowel.
- It includes at least one consonant.
You are given a string word.
Return true if word is valid, otherwise, return false.
Notes:
- 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
- A consonant is an English letter that is not a vowel."""


class Solution:
    @staticmethod
    def isValidWord(word: str) -> bool:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)."""
        # Check if the word has at least 3 characters
        if len(word) < 3:
            return False
        # Define sets for vowels and consonants
        vowels = set("aeiouAEIOU")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        # Initialize flags for vowel and consonant presence
        has_vowel, has_consonant = False, False
        # Iterate through each character in the word
        for char in word:
            # Check if the character is alphanumeric
            if not char.isalnum():
                return False
            # Check if the character is a vowel
            if char in vowels:
                has_vowel = True
            # Check if the character is a consonant
            elif char in consonants:
                has_consonant = True

        # Return true if the word has at least one vowel and one consonant
        return has_vowel and has_consonant


# Unit Test: word = "234Adas", Output = True
assert Solution.isValidWord("234Adas") is True

# Unit Test: word = "b3", Output = False
assert Solution.isValidWord("b3") is False

# Unit Test: word = "a3$e", Output = False
assert Solution.isValidWord("a3$e") is False

# Unit Test: word = "Ya$", Output = False
assert Solution.isValidWord("Ya$") is False

print("All unit tests are passed.")

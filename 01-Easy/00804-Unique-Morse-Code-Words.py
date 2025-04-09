"""804. Unique Morse Code Words
Link: https://leetcode.com/problems/unique-morse-code-words/
Difficulty: Easy
Description: International Morse Code defines a standard encoding where each letter is mapped
to a series of dots and dashes. Return the number of different transformations among
all words we have."""

from typing import List


class Solution:
    @staticmethod
    def uniqueMorseRepresentations(words: List[str]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)"""
        # Morse code
        morse_codes = [".-", "-...", "-.-.", "-..", ".",  # a, b, c, d, e
                       "..-.", "--.", "....", "..", ".---",  # f, g, h, i, j
                       "-.-", ".-..", "--", "-.", "---",  # k, l, m, n, o
                       ".--.", "--.-", ".-.", "...", "-",  # p, q, r, s, t
                       "..-", "...-", ".--", "-..-", "-.--", "--.."]  # u, v, w, x, y, z

        # Use a set to store unique Morse code transformations
        unique_transformations: set[str] = set()

        for word in words:
            # ord(char) - ord('a') is the index of the Morse code for the character
            # ''.join() joins a generator object of strings into a string without separator
            transformation = ''.join(morse_codes[ord(char) - ord('a')] for char in word)
            unique_transformations.add(transformation)

        return len(unique_transformations)


# Input: words = ["gin", "zen", "gig", "msg"], Output: 2
assert Solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2

# Input: words = ["a"], Output: 1
assert Solution.uniqueMorseRepresentations(["a"]) == 1

# Input: words = ["b"], Output: 1
assert Solution.uniqueMorseRepresentations(["b"]) == 1

# Input: words = ["a", "b"], Output: 2
assert Solution.uniqueMorseRepresentations(["a", "b"]) == 2

print("All unit tests are passed.")

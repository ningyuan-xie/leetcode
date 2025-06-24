"""2062. Count Vowel Substrings of a String
Link: https://leetcode.com/problems/count-vowel-substrings-of-a-string/
Difficulty: Easy
Description: A substring is a contiguous (non-empty) sequence of characters within a string.
A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and
has all five vowels present in it.
Given a string word, return the number of vowel substrings in word."""


class Solution:
    @staticmethod
    def countVowelSubstrings(word: str) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n^2), Space Complexity: O(1)."""

        def is_vowel(c):
            """Helper function to check if a character is a vowel"""
            return c in 'aeiou'

        n = len(word)  # Length of the string
        count = 0  # Initialize count of vowel substrings

        # Iterate over all starting indices of substrings
        for start in range(n):
            # Skip if the starting character is not a vowel
            if not is_vowel(word[start]):
                continue  # Skip the current iteration and move to the next start index

            # Track vowels seen in the current substring
            seen_vowels = set()

            # Expand the window and check for valid substrings
            for end in range(start, n):
                if not is_vowel(word[end]):  # Stop if a non-vowel is encountered
                    break  # Break the inner loop and move to the next start index

                seen_vowels.add(word[end])  # Add the vowel to the set

                if len(seen_vowels) == 5:  # All 5 vowels are present
                    count += 1

        return count


# Input: word = "aeiouu", Output: 2
assert Solution.countVowelSubstrings("aeiouu") == 2

# Input: word = "unicornarihan", Output: 0
assert Solution.countVowelSubstrings("unicornarihan") == 0

# Input: word = "cuaieuouac", Output: 7
assert Solution.countVowelSubstrings("cuaieuouac") == 7

print("All unit tests are passed.")

"""1763. Longest Nice Substring
Link: https://leetcode.com/problems/longest-nice-substring/
Difficulty: Easy
Description: A string s is nice if, for every letter of the alphabet that s contains, it appears
both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B'
and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
Given a string s, return the longest substring of s that is nice. If there are multiple, return the
substring of the earliest occurrence. If there are none, return an empty string."""


class Solution:
    @staticmethod
    def longestNiceSubstring(s: str) -> str:
        """Optimal Solution: Recursion. Time Complexity: O(n^2), Space Complexity: O(n^2)."""
        # Base case: If the string has less than 2 characters, it can't be "nice"
        if len(s) < 2:
            return ""

        # Check each character to find the first "bad" character that breaks the "nice" condition
        for i, char in enumerate(s):
            # If the opposite case of the character is not in the string, it's a "bad" character
            if char.swapcase() not in s:
                # Recursively check the substrings on both sides of the "bad" character
                left_nice = Solution.longestNiceSubstring(s[:i])
                right_nice = Solution.longestNiceSubstring(s[i + 1:])
                # Return the longer "nice" substring
                return left_nice if len(left_nice) >= len(right_nice) else right_nice

        # If no "bad" character is found, the entire string is "nice"
        return s


# Unit Test: s = "YazaAay", Output: "aAa"
assert Solution.longestNiceSubstring("YazaAay") == "aAa"

# Unit Test: s = "Bb", Output: "Bb"
assert Solution.longestNiceSubstring("Bb") == "Bb"

# Unit Test: s = "c", Output: ""
assert Solution.longestNiceSubstring("c") == ""

print("All unit tests are passed.")

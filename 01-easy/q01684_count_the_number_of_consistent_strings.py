"""1684. Count the Number of Consistent Strings
Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/
Difficulty: Easy
Description: You are given a string allowed consisting of distinct characters and an array of strings
words. A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words."""

from typing import List


class Solution:
    @staticmethod
    def count_consistent_strings(allowed: str, words: List[str]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the result counter
        result = 0

        # Convert the allowed string to a set for faster lookup
        allowed_set = set(allowed)  # "ab" -> {"a", "b"}

        # Traverse the words array and count the number of consistent strings
        for word in words:
            # Check if all characters in the word are present in the allowed set
            if all(c in allowed_set for c in word):
                result += 1

        return result


# Input: allowed = "ab", words = ["ad", "bd", "aaab", "baa", "badab"], Output: 2
assert Solution.count_consistent_strings("ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2

# Input: allowed = "abc", words = ["a", "b", "c", "ab", "ac", "bc", "abc"], Output: 7
assert Solution.count_consistent_strings("abc", ["a", "b", "c", "ab",
                                                 "ac", "bc", "abc"]) == 7

# Input: allowed = "cad", words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], Output: 4
assert Solution.count_consistent_strings("cad", ["cc", "acd", "b", "ba",
                                                 "bac", "bad", "ac", "d"]) == 4

print("All unit tests are passed.")

"""1768. Merge Strings Alternately
Link: https://leetcode.com/problems/merge-strings-alternately/
Difficulty: Easy
Description: You are given two strings word1 and word2. Merge the strings by adding letters in
alternating order, starting with word1. If a string is longer than the other, append the
additional letters onto the end of the merged string.
Return the merged string."""


class Solution:
    @staticmethod
    def merge_alternately(word1: str, word2: str) -> str:
        """Optimal Solution: One Pass. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the merged string
        merged = []
        # Get the length of the shorter string
        n = min(len(word1), len(word2))

        # Merge the strings alternately up to the length of the shorter string
        for i in range(n):
            merged.append(word1[i])
            merged.append(word2[i])

        # Append the remaining characters from the longer string
        merged.append(word1[n:]) if len(word1) > len(word2) else merged.append(word2[n:])

        # Join the merged characters into a single string
        return "".join(merged)


# Unit Test: word1 = "abc", word2 = "pqr", Output: "apbqcr"
assert Solution.merge_alternately("abc", "pqr") == "apbqcr"

# Unit Test: word1 = "ab", word2 = "pqrs", Output: "apbqrs"
assert Solution.merge_alternately("ab", "pqrs") == "apbqrs"

# Unit Test: word1 = "abcd", word2 = "pq", Output: "apbqcd"
assert Solution.merge_alternately("abcd", "pq") == "apbqcd"

print("All unit tests are passed")

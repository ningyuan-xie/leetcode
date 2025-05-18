"""2506. Count Pairs Of Similar Strings
Link: https://leetcode.com/problems/count-pairs-of-similar-strings/
Difficulty: Easy
Description: You are given a 0-indexed string array words.
Two strings are similar if they consist of the same characters.
- For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
- However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings
words[i] and words[j] are similar."""

from typing import List


class Solution:
    @staticmethod
    def similarPairs(words: List[str]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n * m), Space Complexity: O(n)."""
        # Transform each word into a set of characters
        words = [set(word) for word in words]  # {"a", "b"}, {"a", "b", "c"}, {"a", "b", "c", "d"}

        # Initialize the answer to 0
        ans = 0
        # Iterate through each pair of words
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # Check if the two words are similar
                if words[i] == words[j]:
                    # Increment the answer if they are similar
                    ans += 1
        return ans


# Unit Test: words = ["aba", "aabb", "abcd", "bac", "aabc"], Output: 2
assert Solution.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]) == 2

# Unit Test: words = ["aabb", "ab", "ba"], Output: 3
assert Solution.similarPairs(["aabb", "ab", "ba"]) == 3

# Unit Test: words = ["nba", "cba", "dba"], Output: 0
assert Solution.similarPairs(["nba", "cba", "dba"]) == 0

print("All unit tests are passed.")

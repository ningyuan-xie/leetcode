"""2068. Check Whether Two Strings are Almost Equivalent
Link: https://leetcode.com/problems/Check-Whether-Two-Strings-are-Almost-Equivalent
Difficulty: Easy
Description: Two strings word1 and word2 are considered almost equivalent if the differences
between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.
Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost
equivalent, or false otherwise.
The frequency of a letter x is the number of times it occurs in the string."""


class Solution:
    @staticmethod
    def areAlmostEquivalent(word1: str, word2: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)"""
        # Use dictionaries to store the frequencies of each letter in the two strings
        freq1, freq2 = {}, {}
        for c1, c2 in zip(word1, word2):
            freq1[c1] = freq1.get(c1, 0) + 1
            freq2[c2] = freq2.get(c2, 0) + 1

        # Compare the frequencies of each letter from 'a' to 'z'
        for c in 'abcdefghijklmnopqrstuvwxyz':
            diff = abs(freq1.get(c, 0) - freq2.get(c, 0))
            if diff > 3:
                return False

        return True


# Unit Test: word1 = "aaaa", word2 = "bccb", Output: False
assert Solution.areAlmostEquivalent("aaaa", "bccb") is False

print("All unit tests are passed.")

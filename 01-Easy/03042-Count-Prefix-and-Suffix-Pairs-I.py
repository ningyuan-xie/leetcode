"""3042. Count Prefix and Suffix Pairs I
Link: https://leetcode.com/problems/count-prefix-and-suffix-pairs/
Difficulty: Easy
Description: You are given a 0-indexed string array words.
Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
- isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2,
and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa"
and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
Return an integer denoting the number of index pairs (i, j) such that i < j, and
isPrefixAndSuffix(words[i], words[j]) is true."""

from typing import List


class Solution:
    @staticmethod
    def countPrefixSuffixPairs(words: List[str]) -> int:
        """Optimal Solution: Prefix and Suffix.
           Time Complexity: O(n^2), Space Complexity: O(1)"""
        # Initialize the count of prefix and suffix pairs
        count = 0

        def isPrefixandSuffix(str1: str, str2: str) -> bool:
            """Check if str1 is both a prefix and a suffix of str2"""
            return str2.startswith(str1) and str2.endswith(str1)

        # Iterate through the array and count the number of prefix and suffix pairs
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixandSuffix(words[i], words[j]):
                    count += 1
        return count


# Unit Test: words = ["a","aba","ababa","aa"], Output = 4
assert Solution.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]) == 4

# Unit Test: words = ["pa","papa","ma","mama"], Output = 2
assert Solution.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]) == 2

# Unit Test: words = ["abab","ab"], Output = 0
assert Solution.countPrefixSuffixPairs(["abab", "ab"]) == 0

print("All unit tests are passed.")

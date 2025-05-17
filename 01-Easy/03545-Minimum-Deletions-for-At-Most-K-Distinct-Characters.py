"""3545. Minimum Deletions for At Most K Distinct Characters
Link: https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/
Difficulty: Easy
Description: You are given a string s consisting of lowercase English letters, and an integer k.
Your task is to delete some (possibly none) of the characters in the string so that the number of distinct characters in the resulting string is at most k.
Return the minimum number of deletions required to achieve this."""


class Solution:
    @staticmethod
    def minDeletions(s: str, k: int) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(nlog(n)), Space Complexity: O(n)."""
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Sort the frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)
        deletions = 0

        # Sum the frequencies of characters beyond the first k
        for i in range(k, len(frequencies)):
            deletions += frequencies[i]

        return deletions


def unit_tests():
    # Input: s = "abc", k = 2, Output: 1
    assert Solution.minDeletions("abc", 2) == 1

    # Input: s = "aabb", k = 2, Output: 0
    assert Solution.minDeletions("aabb", 2) == 0

    # Input: s = "yyyzz", k = 1, Output: 2
    assert Solution.minDeletions("yyyzz", 1) == 2


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

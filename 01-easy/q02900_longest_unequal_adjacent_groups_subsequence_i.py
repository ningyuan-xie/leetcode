"""2900. Longest Unequal Adjacent Groups Subsequence I
Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
Difficulty: Easy
Description: You are given a string array words and a binary array groups both of length n, where
words[i] is associated with groups[i].
Your task is to select the longest alternating subsequence from words. A subsequence of words is
alternating if for any two consecutive strings in the sequence, their corresponding elements in
the binary array groups differ. Essentially, you are to choose strings such that adjacent elements
have non-matching corresponding bits in the groups array.
Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted
as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then
find the words corresponding to these indices.
Return the selected subsequence. If there are multiple answers, return any of them.
Note: The elements in words are distinct."""

from typing import List


class Solution:
    @staticmethod
    def getLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
        """Optimal Solution: Greedy. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(words)
        subsequence_index = [0]  # Add the 1st index to the subsequence

        # Find the longest alternating subsequence
        for i in range(1, n):
            if groups[i] != groups[subsequence_index[-1]]:
                subsequence_index.append(i)

        return [words[i] for i in subsequence_index]


# Input: words = ["e","a","b"], groups = [0,0,1], Output: ["e","b"] or ["a","b"]
assert (Solution.getLongestSubsequence(["e", "a", "b"], [0, 0, 1])
        in [["e", "b"], ["a", "b"]])

# Input: words = ["a","b","c","d"], groups = [1,0,1,1], Output: ["a","b","c"] or ["a","b","d"]
assert (Solution.getLongestSubsequence(["a", "b", "c", "d"], [1, 0, 1, 1])
        in [["a", "b", "c"], ["a", "b", "d"]])

print("All unit tests are passed.")

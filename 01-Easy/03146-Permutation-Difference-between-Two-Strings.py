"""3146. Permutation Difference between Two Strings
Link: https://leetcode.com/problems/permutation-difference-between-two-strings
Difficulty: Easy
Description: You are given two strings s and t such that every character occurs at most once in s
and t is a permutation of s.
The permutation difference between s and t is defined as the sum of the absolute difference
between the index of the occurrence of each character in s and the index of the occurrence of
the same character in t.
Return the permutation difference between s and t."""


class Solution:
    @staticmethod
    def permutationDifference(s: str, t: str) -> int:
        """Optimal Solution: .index() method. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the result variable
        result = 0
        # Iterate through each character in the first string
        for i in range(len(s)):
            # Add the absolute difference of the indices to the result
            result += abs(i - t.index(s[i]))

        # Return the final result
        return result


# Unit Test: s = "abc", t = "bac", Output = 2
assert Solution.permutationDifference("abc", "bac") == 2

# Unit Test: s = "abcde", t = "edbac", Output = 12
assert Solution.permutationDifference("abcde", "edbac") == 12

print("All unit tests are passed.")

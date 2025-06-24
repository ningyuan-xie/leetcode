"""1662. Check If Two String Arrays are Equivalent
Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Difficulty: Easy
Description: Given two string arrays word1 and word2, return true if the two arrays represent the
same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string."""

from typing import List


class Solution:
    @staticmethod
    def array_strings_are_equal(word1: List[str], word2: List[str]) -> bool:
        """Optimal Solution: Join and Compare. Time Complexity: O(n), Space Complexity: O(n)."""
        return "".join(word1) == "".join(word2)


# Input: word1 = ["ab", "c"], word2 = ["a", "bc"], Output: True
assert Solution.array_strings_are_equal(["ab", "c"], ["a", "bc"]) is True

# Input: word1 = ["a", "cb"], word2 = ["ab", "c"], Output: False
assert Solution.array_strings_are_equal(["a", "cb"], ["ab", "c"]) is False

# Input: word1 = ["abc", "d", "defg"], word2 = ["abcddefg"], Output: True
assert Solution.array_strings_are_equal(["abc", "d", "defg"], ["abcddefg"]) is True

print("All unit tests are passed.")

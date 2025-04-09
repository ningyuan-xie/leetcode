"""2788. Split Strings by Separator
Link: https://leetcode.com/problems/split-strings-by-separator/
Difficulty: Easy
Description: Given an array of strings words and a character separator, split each string in words
by separator.
Return an array of strings containing the new strings formed after the splits, excluding empty strings.
Notes
- separator is used to determine where the split should occur, but it is not included as part of the
resulting strings.
- A split may result in more than two strings.
- The resulting strings must maintain the same order as they were initially given."""

from typing import List


class Solution:
    @staticmethod
    def splitWordsBySeparator(words: List[str], separator: str) -> List[str]:
        """Optimal Solution: Split. Time Complexity: O(n), Space Complexity: O(n)"""
        result = []

        for word in words:
            strings = word.split(separator)
            for string in strings:
                if string:
                    result.append(string)
        return result


# Unit Test: words = ["one.two.three","four.five","six"], separator = "."
# Output: ["one", "two", "three", "four", "five", "six"]
assert (Solution.splitWordsBySeparator(["one.two.three", "four.five", "six"], ".") ==
        ["one", "two", "three", "four", "five", "six"])

# Unit Test: words = ["$easy$","$problem$"], separator = "$", Output: ["easy", "problem"]
assert Solution.splitWordsBySeparator(["$easy$", "$problem$"], "$") == ["easy", "problem"]

# Unit Test: words = ["|||"], separator = "|", Output: []
assert Solution.splitWordsBySeparator(["|||"], "|") == []

print("All unit tests are passed.")

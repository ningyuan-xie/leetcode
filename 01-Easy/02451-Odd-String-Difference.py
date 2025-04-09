"""2451. Odd String Difference
Link: https://leetcode.com/problems/odd-string-difference/
Difficulty: Easy
Description: You are given an array of equal-length strings words. Assume that the length of each
string is n.
Each string words[i] can be converted into a difference integer array difference[i] of length n - 1
where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference
between two letters is the difference between their positions in the alphabet i.e. the position of 'a'
is 0, 'b' is 1, and 'z' is 25.
- For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.
Return the string in words that has different difference integer array."""

from typing import List


class Solution:
    @staticmethod
    def oddString(words: List[str]) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""

        def get_diff(s: str) -> str:
            """Helper function to get the difference between adjacent characters"""
            result = []
            for i in range(len(s) - 1):
                result.append(str(ord(s[i + 1]) - ord(s[i])))
            # E.g. "adc" -> [3, -1] -> "3, -1", need string because list is mutable and cannot be key
            return ", ".join(result)

        diff_map = {}
        for word in words:
            diff = get_diff(word)
            diff_map[diff] = diff_map.get(diff, []) + [word]
        # E.g. {'3, -1': ['adc', 'wzy'], '1, 1': ['abc']}

        for (key, value) in diff_map.items():
            if len(value) == 1:
                return value[0]


# Unit Test: words = ["adc", "wzy", "abc"], Output: "abc"
assert Solution.oddString(["adc", "wzy", "abc"]) == "abc"

# Unit Test: words = ["aaa", "bob", "ccc", "ddd"], Output: "bob"
assert Solution.oddString(["aaa", "bob", "ccc", "ddd"]) == "bob"

print("All unit tests are passed.")

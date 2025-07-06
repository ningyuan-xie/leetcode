"""14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Description: Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""."""

from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        """Optimal Solution: Horizontal scanning. Time Complexity: O(n*m), Space Complexity: O(1)."""
        # Check if the list is empty
        if not strs:
            return ""

        # Initialize the prefix to the first string
        prefix = strs[0]

        # Loop through the rest of the strings
        for s in strs[1:]:
            # Compare the prefix with each string
            while not s.startswith(prefix):
                # Reduce the prefix by one character from the end
                prefix = prefix[:-1]
                # If the prefix becomes empty, return ""
                if not prefix:
                    return ""

        return prefix


def unit_tests():
    # Input: strs = ["flower", "flow", "flight"], Output: "fl"
    assert Solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

    # Input: strs = ["dog", "racecar", "car"], Output: ""
    assert Solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""

    # Input: strs = ["c","acc","ccc"], Output: ""
    assert Solution.longestCommonPrefix(["c", "acc", "ccc"]) == ""


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

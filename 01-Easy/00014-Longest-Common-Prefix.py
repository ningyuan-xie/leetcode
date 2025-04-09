"""14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Description: Write a function to find the longest common prefix string amongst
an array of strings."""

from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        """Optimal Solution: Horizontal Scanning.
           Time Complexity: O(n * m), Space Complexity: O(1)."""
        # Initialize prefix
        prefix = ""
        # If the list is empty, return an empty string
        if not strs:
            return prefix
        # Use first string in the list as the reference string: loop through its index
        first_str = strs[0]  # E.g. "flower"
        for i in range(len(first_str)):  # E.g. i = 0, 1, 2, 3, 4, 5
            # Loop through the rest of the strings in the list
            for current_str in strs:  # E.g. "flow", "flight": s = "flow", "flight"
                # Return the prefix if the current index reaches the length of the current string,
                # or the current string's character does not match the character in the first string,
                if i == len(current_str) or first_str[i] != current_str[i]:
                    return prefix
            # Otherwise, add the current character to the prefix
            prefix += first_str[i]
        return prefix


# Input: strs = ["flower", "flow", "flight"], Output: "fl"
assert Solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

# Input: strs = ["dog", "racecar", "car"], Output: ""
assert Solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""

# Input: strs = ["c","acc","ccc"], Output: ""
assert Solution.longestCommonPrefix(["c", "acc", "ccc"]) == ""

print("All unit tests are passed.")

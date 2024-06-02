# Link: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Description: Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    @staticmethod
    def longestCommonPrefix(strs: list[str]) -> str:
        # Initialize prefix
        prefix = ""
        # If the list is empty, return an empty string
        if not strs:
            return prefix
        # Loop through the index of characters in the first string in the list
        for i in range(len(strs[0])):  # E.g. "flower": i = 0, 1, 2, 3, 4, 5
            # Loop through the rest of the strings in the list
            for j in range(1, len(strs)):  # E.g. "flow", "flight": j = 1, 2
                # If the current index i > the length of the current string,
                # or the current string's character does not match the character in the first string,
                # return the prefix
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return prefix
            # Otherwise, add the current character to the prefix
            prefix += strs[0][i]
        return prefix


# Unit Test: Input: strs = ["flower", "flow", "flight"], Output: "fl"
assert Solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

# Unit Test: Input: strs = ["dog", "racecar", "car"], Output: ""
assert Solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""

# Unit Test: Input: strs = ["c","acc","ccc"], Output: ""
assert Solution.longestCommonPrefix(["c", "acc", "ccc"]) == ""
print("All unit tests are passed")

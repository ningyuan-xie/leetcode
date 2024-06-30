# Link: https://leetcode.com/problems/isomorphic-strings/
# Difficulty: Easy
# Description: Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.


class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        # Initialize two dictionaries to store the mapping of characters
        s2t = {}
        t2s = {}
        # Iterate through the strings
        for c1, c2 in zip(s, t):  # zip function is used to iterate through two strings simultaneously
            # Check if the mutual mapping is violated
            if (c1 in s2t and s2t[c1] != c2) or (c2 in t2s and t2s[c2] != c1):
                return False
            # Update the mapping
            s2t[c1] = c2  # s2t: {'f': 'b', 'o': 'a'}
            t2s[c2] = c1  # t2s: {'b': 'f', 'a': 'o'}
        return True


# Unit Test: Input: s = "egg", t = "add", Output: True
assert Solution.isIsomorphic("egg", "add") == True

# Unit Test: Input: s = "foo", t = "bar", Output: False
assert Solution.isIsomorphic("foo", "bar") == False

# Unit Test: Input: s = "paper", t = "title", Output: True
assert Solution.isIsomorphic("paper", "title") == True

print("All unit tests are passed")

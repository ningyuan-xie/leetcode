"""2839. Check if Strings Can Be Made Equal With Operations I
Link: https://leetcode.com/problems/check-if-strings-can-be-made-equal/
Difficulty: Easy
Description: You are given two strings s1 and s2, both of length 4, consisting of lowercase English
letters.
You can apply the following operation on any of the two strings any number of times:
- Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices
in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise."""


class Solution:
    @staticmethod
    def canBeEqual(s1: str, s2: str) -> bool:
        """Optimal Solution: Sort Even and Odd Indexed Characters.
           Time Complexity: O(nlog(n)), Space Complexity: O(1)
           Same as 2840. Check if Strings Can Be Made Equal With Operations II"""
        # Extract even and odd indexed characters
        even_s1 = sorted(s1[i] for i in range(0, len(s1), 2))
        even_s2 = sorted(s2[i] for i in range(0, len(s2), 2))
        odd_s1 = sorted(s1[i] for i in range(1, len(s1), 2))
        odd_s2 = sorted(s2[i] for i in range(1, len(s2), 2))

        # Check if both sorted sets match
        return even_s1 == even_s2 and odd_s1 == odd_s2


# Unit Test: s1 = "abcd", s2 = "cdab", Output: True
assert Solution.canBeEqual("abcd", "cdab") is True

# Unit Test: s1 = "abcd", s2 = "dacb", Output: False
assert Solution.canBeEqual("abcd", "dacb") is False

# Unit Test: s1 = "abcdba", s2 = "cabdab", Output: True
assert Solution.canBeEqual("abcdba", "cabdab") is True

# Unit Test: s1 = "abe", s2 = "bea", Output: False
assert Solution.canBeEqual("abe", "bea") is False

print("All unit tests are passed.")

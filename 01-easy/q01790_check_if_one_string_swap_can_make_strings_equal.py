"""1790. Check if One String Swap Can Make Strings Equal
Link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
Difficulty: Easy
Description: You are given two strings s1 and s2 of equal length. A string swap is an operation
where you choose two indices in a string (not necessarily different) and swap the characters at
these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on
exactly one of the strings. Otherwise, return false."""


class Solution:
    @staticmethod
    def can_strings_equal(s1: str, s2: str) -> bool:
        """Optimal Solution: Check for exactly two differences.
           Time Complexity: O(n), Space Complexity: O(1)."""
        # If strings are already equal, no swap is needed
        if s1 == s2:
            return True

        # Find indices where the strings differ: E.g. "bank" and "kanb" -> [(b, k), (k, b)]
        differences = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]

        # Check if exactly two differences exist and swapping resolves the issue
        return len(differences) == 2 and differences[0] == differences[1][::-1]


# Unit Test: s1 = "bank", s2 = "kanb", Output: True
assert Solution.can_strings_equal("bank", "kanb") is True

# Unit Test: s1 = "attack", s2 = "defend", Output: False
assert Solution.can_strings_equal("attack", "defend") is False

# Unit Test: s1 = "kelb", s2 = "kelb", Output: True
assert Solution.can_strings_equal("kelb", "kelb") is True

print("All unit tests are passed.")

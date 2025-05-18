"""205. Isomorphic Strings
Link: https://leetcode.com/problems/isomorphic-strings/
Difficulty: Easy
Description: Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself."""


class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize two dictionaries to store character mappings
        s_to_t = {}
        t_to_s = {}

        # Iterate through both strings simultaneously
        for char_s, char_t in zip(s, t):
            # Check if the mapping exists in both dictionaries
            if (char_s in s_to_t and s_to_t[char_s] != char_t
                or char_t in t_to_s and t_to_s[char_t] != char_s):
                # If the mapping is inconsistent, return False
                return False

            # Create the mapping if it doesn't exist
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True


def unit_tests():
    # Input: s = "egg", t = "add", Output: True
    assert Solution.isIsomorphic("egg", "add") is True

    # Input: s = "foo", t = "bar", Output: False
    assert Solution.isIsomorphic("foo", "bar") is False

    # Input: s = "paper", t = "title", Output: True
    assert Solution.isIsomorphic("paper", "title") is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""459. Repeated Substring Pattern
Link: https://leetcode.com/problems/repeated-substring-pattern/
Difficulty: Easy
Description: Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together."""


class Solution:
    @staticmethod
    def repeatedSubstringPattern(s: str) -> bool:
        """Optimal Solution: String Rotation. Time Complexity: O(n), Space Complexity: O(1).
        If s can be formed by repeating a substring, then its rotation will appear inside (s + s)[1:-1]."""
        return s in (s + s)[1:-1]


def unit_tests():
    # Input: s = "abab", Output: True
    assert Solution.repeatedSubstringPattern("abab") is True

    # Input: s = "aba", Output: False
    assert Solution.repeatedSubstringPattern("aba") is False

    # Input: s = "abcabcabcabc", Output: True
    assert Solution.repeatedSubstringPattern("abcabcabcabc") is True

    # Input: s = "abaababaab", Output: True
    assert Solution.repeatedSubstringPattern("abaababaab") is True

    # Input: s = "ababba", Output: False
    assert Solution.repeatedSubstringPattern("ababba") is False

    # Input: s = "ababab", Output: True
    assert Solution.repeatedSubstringPattern("ababab") is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""3407. Substring Matching Pattern
Link: https://leetcode.com/problems/substring-matching-pattern/
Difficulty: Easy
Description: You are given a string s and a pattern string p, where p contains exactly one '*' character.
The '*' in p can be replaced with any sequence of zero or more characters.
Return true if p can be made a substring of s, and false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def isSubstringMatchingPattern(s: str, p: str) -> bool:
        """Optimal Solution: Prefix and Suffix Match. Time Complexity: O(n^2), Space Complexity: O(1)."""
        # Split the pattern into prefix and suffix around the '*'
        prefix, suffix = p.split('*')

        for i in range(len(s) - len(prefix) - len(suffix) + 1):
            # Check if the prefix and suffix match the respective positions
            if s[i:i+len(prefix)] == prefix:
                for j in range(i + len(prefix), len(s) - len(suffix) + 1):
                    if s[j:j+len(suffix)] == suffix:
                        return True
        return False


def unit_tests():
    # Input: s = "leetcode", p = "ee*e", Output: True
    assert Solution.isSubstringMatchingPattern("leetcode", "ee*e") is True

    # Input: s = "car", p = "c*v", Output: False
    assert Solution.isSubstringMatchingPattern("car", "c*v") is False
    
    # Input: s = "luck", p = "u*", Output: True
    assert Solution.isSubstringMatchingPattern("luck", "u*") is True

    # Input: s = "jjv", p = "*j", Output: True
    assert Solution.isSubstringMatchingPattern("jjv", "*j") is True

if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

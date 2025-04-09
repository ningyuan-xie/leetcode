"""2124. Check if All As Appears Before All Bs
Link: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs
Difficulty: Easy
Description: Given a string s consisting of only the characters 'a' and 'b', return true if every
'a' appears before every 'b' in the string. Otherwise, return false."""


class Solution:
    @staticmethod
    def allAsBeforeBs(s: str) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)"""
        n = len(s)

        for i in range(n - 1):
            if s[i] == 'b' and s[i + 1] == 'a':
                return False
        return True


# Unit Test: s = "aaabbb", Output: True
assert Solution.allAsBeforeBs("aaabbb") is True

# Unit Test: s = "abab", Output: False
assert Solution.allAsBeforeBs("abab") is False

# Unit Test: s = "bbb", Output: True
assert Solution.allAsBeforeBs("bbb") is True

print("All unit tests are passed.")

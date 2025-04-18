"""3456. Find Special Substring of Length K
Link: https://leetcode.com/problems/find-special-substring-of-length-k/
Difficulty: Easy
Description: You are given a string s and an integer k.
Determine if there exists a substring of length exactly k in s that satisfies the following conditions:
1. The substring consists of only one distinct character (e.g., "aaa" or "bbb").
2. If there is a character immediately before the substring, it must be different from the character in the substring.
3. If there is a character immediately after the substring, it must also be different from the character in the substring.
Return true if such a substring exists. Otherwise, return false."""


class Solution:
    @staticmethod
    def hasSpecialSubstring(s: str, k: int) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(s)
        if k > n:
            return False

        for i in range(n - k + 1):
            substring = s[i:i + k]
            # Check each condition for the substring
            if (len(set(substring)) == 1 
                and (i == 0 or s[i - 1] != substring[0]) 
                and (i + k == n or s[i + k] != substring[0])):
                return True

        return False


def unit_tests():
    # Input: s = "aaabaaa", k = 3, Output: True
    assert Solution.hasSpecialSubstring("aaabaaa", 3) is True

    # Input: s = "abc", k = 2, Output: False
    assert Solution.hasSpecialSubstring("abc", 2) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""459. Repeated Substring Pattern
Link: https://leetcode.com/problems/repeated-substring-pattern/
Difficulty: Easy
Description: Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together."""


class Solution:
    @staticmethod
    def repeatedSubstringPattern(s: str) -> bool:
        """Sub-Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(n)"""
        # Substring's length ranges from 1 to len(s) // 2 + 1
        for i in range(1, len(s) // 2 + 1):  # O(n/2). E.g. s = "abab", i = 1, 2
            # If the length of the substring divides the length of the string
            if len(s) % i == 0:
                # Construct the substring by repeating the first i characters
                substring = s[:i]
                # Recover the string by repeating the substring: O(n)
                repeated_string = substring * (len(s) // i)  # i = 1, "aaaa" -> i = 2, "abab"
                # Compare the recovered string with the original string: O(n)
                if repeated_string == s:
                    return True
        return False


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

print("All unit tests are passed.")

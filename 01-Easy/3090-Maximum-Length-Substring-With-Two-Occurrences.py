"""3090. Maximum Length Substring With Two Occurrences
Link: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
Difficulty: Easy
Description: Given a string s, return the maximum length of a substring such that it contains at most
two occurrences of each character."""


class Solution:
    @staticmethod
    def maximumLengthSubstring(s: str) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(1)"""
        max_length = 0

        def isSubstringValid(substring: str) -> bool:
            """Helper function to check if the substring is valid"""
            char_count = {}
            for char in substring:
                char_count[char] = char_count.get(char, 0) + 1
                if char_count[char] > 2:
                    return False
            return True

        # Iterate through all possible substrings and find the maximum length
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if isSubstringValid(s[i:j]):
                    max_length = max(max_length, j - i)

        return max_length


# Unit Test: s = "bcbbbcba", Output = 4
assert Solution.maximumLengthSubstring("bcbbbcba") == 4

# Unit Test: s = "aaaa", Output = 2
assert Solution.maximumLengthSubstring("aaaa") == 2

print("All unit tests are passed")

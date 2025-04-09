"""1332. Remove Palindromic Subsequences
Link: https://leetcode.com/problems/remove-palindromic-subsequences
Difficulty: Easy
Description: Given a string s consisting only of letters 'a' and 'b'.
In a single step you can remove one palindromic subsequence from s.
Return the minimum number of steps to make the given string empty."""


class Solution:
    @staticmethod
    def removePalindromeSub(s: str) -> int:
        """Optimal Solution: A string containing only 'a' and 'b' is a palindrome if it is empty,
           contains only 'a', or contains only 'b'. Thus, the minimum number of steps to make the
           string empty is 1 if the string is a palindrome and 2 otherwise.
           Time Complexity: O(n), Space Complexity: O(1)"""
        # Check if the string is empty, contains only 'a', or contains only 'b'
        return 0 if s == "" else 1 if s == s[::-1] else 2


# Unit Test: s = "ababa", Output: 1
# Explanation: Remove the only palindromic subsequence "aba" to make the string empty.
assert Solution.removePalindromeSub("ababa") == 1

# Unit Test: s = "abb", Output: 2
# Explanation: Remove the palindromic subsequence "bb" first, then remove "a" to make the string empty.
assert Solution.removePalindromeSub("abb") == 2

# Unit Test: s = "baabb", Output: 2
# Explanation: Remove the palindromic subsequence "baab" first then remove "b" to make the string empty.
assert Solution.removePalindromeSub("baabb") == 2

# Unit Test: s = "", Output: 0
# Explanation: The string is already empty.
assert Solution.removePalindromeSub("") == 0

print("All unit tests are passed.")

"""2697. Lexicographically Smallest Palindrome
Link: https://leetcode.com/problems/lexicographically-smallest-palindrome/
Difficulty: Easy
Description: You are given a string s consisting of lowercase English letters, and you are allowed to
perform operations on it. In one operation, you can replace a character in s with another lowercase
English letter.
Your task is to make s a palindrome with the minimum number of operations possible. If there are
multiple palindromes that can be made using the minimum number of operations, make the
lexicographically smallest one.
A string a is lexicographically smaller than a string b (of the same length) if in the first position
where a and b differ, string a has a letter that appears earlier in the alphabet than the
corresponding letter in b.
Return the resulting palindrome string."""


class Solution:
    @staticmethod
    def makeSmallestPalindrome(s: str) -> str:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the list to track the characters
        chars = list(s)
        # Initialize the pointers to track the characters
        left, right = 0, len(chars) - 1

        # Continue the loop until the pointers meet
        while left < right:
            # If the characters are not the same
            if chars[left] != chars[right]:
                chars[left] = chars[right] = min(chars[left], chars[right])
            # Move the pointers
            left += 1
            right -= 1

        # Return the palindrome string
        return "".join(chars)


# Unit Test: s = "egcfe", Output: "efcfe"
assert Solution.makeSmallestPalindrome("egcfe") == "efcfe"

# Unit Test: s = "abcd", Output: "abba"
assert Solution.makeSmallestPalindrome("abcd") == "abba"

# Unit Test: s = "seven", Output: "neven"
assert Solution.makeSmallestPalindrome("seven") == "neven"

print("All unit tests are passed.")

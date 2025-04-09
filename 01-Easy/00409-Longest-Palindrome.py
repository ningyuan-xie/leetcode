"""409. Longest Palindrome
Link: https://leetcode.com/problems/longest-palindrome/
Difficulty: Easy
Description: Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters."""


class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0389-Find-the-Difference.py"""
        # Initialize a dictionary to store the frequency of each character
        char_freq = {}
        # Initialize a variable to store the length of the longest palindrome
        longest_palindrome = 0
        # Iterate through each character in the string
        for char in s:
            # Increment the frequency of the character
            char_freq[char] = char_freq.get(char, 0) + 1
            # If the frequency of the char is even, add it to the length of the longest palindrome
            if char_freq[char] % 2 == 0:
                longest_palindrome += 2
        # If there are any chars with odd frequency, add 1 to the length of the longest palindrome
        for freq in char_freq.values():
            if freq % 2 == 1:
                longest_palindrome += 1
                break  # break out of the loop since we only need to add 1 to the length
        return longest_palindrome


# Unit Test: Input: s = "abccccdd", Output: 7
assert Solution.longestPalindrome("abccccdd") == 7

# Unit Test: Input: s = "a", Output: 1
assert Solution.longestPalindrome("a") == 1

# Unit Test: Input: s = "bb", Output: 2
assert Solution.longestPalindrome("bb") == 2

print("All unit tests are passed")

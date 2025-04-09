"""242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word formed by rearranging the letters of another, such as cinema,
formed from iceman."""


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)"""
        # Base case: if the lengths of two strings are different, return False
        if len(s) != len(t):
            return False
        # Initialize a hash table to store the frequency of characters in string s
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1  # E.g., char_freq = {'a': 3, 'n': 1}
        # Traverse string t and decrement the frequency of characters in the hash table
        for char in t:
            # If the character is in the hash table and the frequency is greater than 0
            if char in char_freq and char_freq[char] > 0:
                # Decrement the frequency of the character in the hash table after using it
                char_freq[char] -= 1
            else:
                return False
        return True


# Input: s = "anagram", t = "nagaram"
assert Solution.isAnagram("anagram", "nagaram") is True

# Input: s = "rat", t = "car"
assert Solution.isAnagram("rat", "car") is False

# Input: s = "a", t = "ab"
assert Solution.isAnagram("a", "ab") is False

print("All unit tests are passed.")

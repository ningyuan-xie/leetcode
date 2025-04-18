"""389. Find the Difference
Link: https://leetcode.com/problems/find-the-difference/
Difficulty: Easy
Description: You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t."""


class Solution:
    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0383-Ransom-Note.py"""
        # Initialize a hash table to store the frequency of characters in string s
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1  # E.g., char_freq = {'a': 1, 'b': 1}
        # Traverse string t and decrement the frequency of characters in the hash table
        for char in t:
            # If the character is in the hash table and the frequency is greater than 0
            if char in char_freq and char_freq[char] > 0:
                # Decrement the frequency of the character in the hash table after using it
                char_freq[char] -= 1
            else:
                return char
        return ""


# Input: s = "abcd", t = "abcde", Output: "e"
assert Solution.findTheDifference("abcd", "abcde") == "e"

# Input: s = "", t = "y", Output: "y"
assert Solution.findTheDifference("", "y") == "y"

# Input: s = "a", t = "aa", Output: "a"
assert Solution.findTheDifference("a", "aa") == "a"

print("All unit tests are passed.")

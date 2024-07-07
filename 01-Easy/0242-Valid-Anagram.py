# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram is a word formed by rearranging the letters of another, such as cinema, formed from iceman.

class Solution:
    # Optimal Solution: Using Hash Table. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        # Base case: if the lengths of two strings are different, return False
        if len(s) != len(t):
            return False

        # Initialize a hash table to store the frequency of characters in string s
        hash_table = {}
        # Traverse string s and store the frequency of characters in the hash table
        for char in s:
            hash_table[char] = hash_table.get(char, 0) + 1

        # Traverse string t and decrement the frequency of characters in the hash table
        for char in t:
            # If the character is not in the hash table, return False
            if char not in hash_table:
                return False
            # Decrement the frequency of the character in the hash table
            hash_table[char] -= 1
            # If the frequency of the character is less than 0,
            if hash_table[char] < 0:
                return False

        return True


# Unit Test: Input: s = "anagram", t = "nagaram"
assert Solution.isAnagram("anagram", "nagaram") is True

# Unit Test: Input: s = "rat", t = "car"
assert Solution.isAnagram("rat", "car") is False

# Unit Test: Input: s = "a", t = "ab"
assert Solution.isAnagram("a", "ab") is False

print("All unit tests are passed")

"""383. Ransom Note
Link: https://leetcode.com/problems/ransom-note/
Difficulty: Easy
Description: Given two strings ransomNote and magazine, return true
if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote."""


class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)
           Similar to 0350-Intersection-of-Two-Arrays-II.py"""
        # Create a hash table to store the frequency of each character in the magazine
        char_freq = {}
        for char in magazine:
            char_freq[char] = char_freq.get(char, 0) + 1  # E.g., char_freq = {'a': 2, 'b': 1}
        # Iterate through the ransom note to check if the magazine can construct the ransom note
        for char in ransomNote:
            # If the character is in the hash table and the frequency is greater than 0
            if char in char_freq and char_freq[char] > 0:
                # Decrement the frequency of the character in the hash table after using it
                char_freq[char] -= 1
            else:
                return False
        return True


# Unit Test: Input: ransomNote = "a", magazine = "b", Output: False
assert Solution.canConstruct("a", "b") == False

# Unit Test: Input: ransomNote = "aa", magazine = "ab", Output: False
assert Solution.canConstruct("aa", "ab") == False

# Unit Test: Input: ransomNote = "aa", magazine = "aab", Output: True
assert Solution.canConstruct("aa", "aab") == True

print("All unit tests are passed")

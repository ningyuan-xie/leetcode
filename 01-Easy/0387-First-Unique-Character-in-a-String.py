# Link: https://leetcode.com/problems/first-unique-character-in-a-string/
# Difficulty: Easy
# Description: Given a string s, return the first non-repeating character
# in it and return its index. If it does not exist, return -1.

class Solution:
    # Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)
    # Similar to 0383-Ransom-Note.py
    @staticmethod
    def firstUniqChar(s: str) -> int:
        # Initialize a hash table to store the frequency of characters in the string
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1  # E.g., char_freq = {'l': 1, 'e': 3}
        # Traverse the string to find the first non-repeating character
        for i, char in enumerate(s):
            if char_freq[char] == 1:
                return i
        return -1


# Unit Test: Input: s = "leetcode", Output: 0
assert Solution.firstUniqChar("leetcode") == 0

# Unit Test: Input: s = "loveleetcode", Output: 2
assert Solution.firstUniqChar("loveleetcode") == 2

# Unit Test: Input: s = "aabb", Output: -1
assert Solution.firstUniqChar("aabb") == -1

print("All unit tests are passed")

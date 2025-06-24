"""1624. Largest Substring Between Two Equal Characters
Link: https://leetcode.com/problems/largest-substring-between-two-equal-characters/
Difficulty: Easy
Description: Given a string s, return the length of the longest substring between two equal
characters, excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string."""


class Solution:
    @staticmethod
    def maxLengthBetweenEqualCharacters(s: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the maximum length of the substring between two equal characters
        max_length = -1

        # Initialize the hash table to store the index of the first occurrence of each character
        first_occurrence = {}

        # Iterate through each character in the string
        for i, char in enumerate(s):
            # If the character is already in the hash table, update the maximum length
            if char in first_occurrence:
                max_length = max(max_length, i - first_occurrence[char] - 1)
            else:
                # Otherwise, add the character to the hash table
                first_occurrence[char] = i  # E.g. s = "abca", first_occurrence = {'a': 0, 'b': 1}

        return max_length


# Input: s = "aa", Output: 0
assert Solution.maxLengthBetweenEqualCharacters("aa") == 0

# Input: s = "abca", Output: 2
assert Solution.maxLengthBetweenEqualCharacters("abca") == 2

# Input: s = "cbzxy", Output: -1
assert Solution.maxLengthBetweenEqualCharacters("cbzxy") == -1

print("All unit tests are passed.")

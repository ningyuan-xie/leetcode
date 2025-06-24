"""1897. Redistribute Characters to Make All Strings Equal
Link: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
Difficulty: Easy
Description: You are given an array of strings words (0-indexed).
In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move
any character from words[i] to any position in words[j].
Return true if you can make every string in words equal using any number of operations, and false
otherwise."""

from typing import List


class Solution:
    @staticmethod
    def makeEqual(words: List[str]) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n * m), Space Complexity: O(1)."""
        # Count the frequency of each character in all words
        char_count = {}
        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1

        # Check if the frequency of each character is divisible by the number of words
        for count in char_count.values():
            if count % len(words) != 0:
                return False
        return True


# Input: words = ["abc", "aabc", "bc"], Output: True
assert Solution.makeEqual(["abc", "aabc", "bc"]) is True

# Input: words = ["ab", "a"], Output: False
assert Solution.makeEqual(["ab", "a"]) is False

print("All unit tests are passed.")

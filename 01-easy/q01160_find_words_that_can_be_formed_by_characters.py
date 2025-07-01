"""1160. Find Words That Can Be Formed by Characters
Link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Difficulty: Easy
Description: You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).
Return the sum of lengths of all good strings in words."""

from typing import List


class Solution:
    @staticmethod
    def countCharacters(words: List[str], chars: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Count characters in chars
        char_count = {}
        for char in chars:
            char_count[char] = char_count.get(char, 0) + 1

        total_length = 0

        # Check each word
        for word in words:
            # Create a copy of char_count to avoid modifying the original
            available_chars = char_count.copy()
            can_form = True
            
            # Check if we can form the word
            for char in word:
                if available_chars.get(char, 0) > 0:
                    available_chars[char] -= 1
                else:
                    can_form = False
                    break
            
            if can_form:
                total_length += len(word)

        return total_length


def unit_tests():
    # Input: words = ["cat", "bt", "hat", "tree"], chars = "atach", Output: 6
    assert Solution.countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6

    # Input: words = ["hello", "world", "leetcode"], chars = "welldonehoneyr", Output: 10
    assert Solution.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr") == 10

    # Input: words = ["cat", "bt", "hat", "tree"], chars = "atach", Output: 6
    assert Solution.countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

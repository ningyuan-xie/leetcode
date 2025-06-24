"""1832. Check if the Sentence Is Pangram
Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
Difficulty: Easy
Description: A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a
pangram, or false otherwise."""


class Solution:
    @staticmethod
    def checkIfPangram(sentence: str) -> bool:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)."""
        # Return True if the number of unique characters is equal to 26
        return len(set(sentence)) == 26


# Input: sentence = "thequickbrownfoxjumpsoverthelazydog", Output: True
assert Solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") is True

# Input: sentence = "leetcode", Output: False
assert Solution.checkIfPangram("leetcode") is False

print("All unit tests are passed.")

"""1941. Check if All Characters Have Equal Number of Occurrences
Link: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
Difficulty: Easy
Description: Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences
(i.e., the same frequency)."""


class Solution:
    @staticmethod
    def areOccurrencesEqual(s: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
        # Count the frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Check if all frequencies are the same using set()
        return len(set(freq.values())) == 1


# Unit Test: s = "abacbc", Output: True
assert Solution.areOccurrencesEqual("abacbc") is True

# Unit Test: s = "aaabb", Output: False
assert Solution.areOccurrencesEqual("aaabb") is False

# Unit Test: s = "a", Output: True
assert Solution.areOccurrencesEqual("a") is True

print("All unit tests are passed.")

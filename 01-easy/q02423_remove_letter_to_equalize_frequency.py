"""2423. Remove Letter To Equalize Frequency
Link: https://leetcode.com/problems/remove-letter-to-equalize-frequency/
Difficulty: Easy
Description: You are given a 0-indexed string word, consisting of lowercase English letters. You need to
select one index and remove the letter at that index from word so that the frequency of every letter
present in word is equal.
Return true if it is possible to remove one letter so that the frequency of all letters in word are
equal, and false otherwise.
Note:
- The frequency of a letter x is the number of times it occurs in the string.
- You must remove exactly one letter and cannot choose to do nothing."""


class Solution:
    @staticmethod
    def equalFrequency(word: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
        # Count the frequency of each character in the word
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1  # E.g. "abcc" -> freq = {'a': 1, 'b': 1, 'c': 2}

        # Count how many times each frequency appears
        freq_count = {}
        for count in freq.values():
            freq_count[count] = freq_count.get(count, 0) + 1  # E.g. "abcc" -> freq_count = {1: 2, 2: 1}

        # Case 1: All characters have the same frequency
        # If there's only one frequency, it must be 1 or appear only once to be valid
        if len(freq_count) == 1:  # "zz" -> {'z': 2} -> {2: 1}; "bac" -> {'b': 1, 'a': 1, 'c': 1} -> {1: 3}
            return 1 in freq_count.keys() or 1 in freq_count.values()

        # Case 2: There are exactly two different frequencies
        if len(freq_count) == 2:
            # Sort frequencies for easier comparison
            (f1, c1), (f2, c2) = sorted(freq_count.items())  # E.g. "abcc" -> (1, 2), (2, 1)

            # Case 2a: One character occurs only once and can be removed
            if f1 == 1 and c1 == 1:  # E.g. "abbcc" -> {'a': 1, 'b': 2, 'c': 2} -> {1: 1, 2: 2}
                return True

            # Case 2b: Higher frequency exceeds the lower by 1 and appears only once
            if f2 - f1 == 1 and c2 == 1:  # E.g. "abcc" -> {'a': 1, 'b': 1, 'c': 2} -> {1: 2, 2: 1}
                return True

        # If none of the conditions are met, it's not possible to equalize frequencies
        return False


# Input: word = "abcc", Output: True
assert Solution.equalFrequency("abcc") is True

# Input: word = "aazz", Output: False
assert Solution.equalFrequency("aazz") is False

# Input: word = "abbcc", Output: True
assert Solution.equalFrequency("abbcc") is True

# Input: word = "a", Output: True
assert Solution.equalFrequency("a") is True

# Input: word = "zz", Output: True
assert Solution.equalFrequency("zz") is True

# Input: word = "bac", Output: True
assert Solution.equalFrequency("bac") is True

print("All unit tests are passed.")

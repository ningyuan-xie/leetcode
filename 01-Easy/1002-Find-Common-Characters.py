"""102. Find Common Characters
Link: https://leetcode.com/problems/find-common-characters/
Difficulty: Easy
Description: Given a string array words, return an array of all characters that show up in all
strings within the words (including duplicates). You may return the answer in any order."""

from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def commonChars(words: List[str]) -> List[str]:
        """Optimal Solution: Counter. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize a counter with the characters from the first word
        # E.g. words = ["bella", "label", "roller"] -> Counter({'b': 1, 'e': 1, 'l': 2, 'a': 1})
        common_count = Counter(words[0])

        # Update the common count by intersecting with each subsequent word's character count
        for word in words[1:]:
            # & operator returns the intersection of two counters
            # E.g. words = ["bella", "label", "roller"] -> Counter({'l': 2, 'e': 1})
            common_count &= Counter(word)

        # Convert the counter back to a list of characters
        # .elements() returns an iterator over elements repeating each as many times as its count
        return list(common_count.elements())


# Unit Test: words = ["bella","label","roller"], Output: ["e","l","l"]
assert Solution.commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]

# Unit Test: words = ["cool","lock","cook"], Output: ["c","o"]
assert Solution.commonChars(["cool", "lock", "cook"]) == ["c", "o"]

print("All unit tests are passed")

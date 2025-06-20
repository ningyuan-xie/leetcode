"""102. Find Common Characters
Link: https://leetcode.com/problems/find-common-characters/
Difficulty: Easy
Description: Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order."""

from typing import List


class Solution:
    @staticmethod
    def commonChars(words: List[str]) -> List[str]:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize dictionary with character counts from first word
        common_chars = {}
        for c in words[0]:
            common_chars[c] = common_chars.get(c, 0) + 1
            
        # For each subsequent word
        for word in words[1:]:
            # Count characters in current word
            curr_chars = {}
            for c in word:
                curr_chars[c] = curr_chars.get(c, 0) + 1
                
            # Keep only characters that appear in both, with minimum count
            new_common = {}
            for c in common_chars:
                if c in curr_chars:
                    new_common[c] = min(common_chars[c], curr_chars[c])
            common_chars = new_common
            
        # Convert dictionary back to list of characters
        result = []
        for c in common_chars:
            result.extend([c] * common_chars[c])
            
        return result


def unit_tests():
    # Unit Test: words = ["bella","label","roller"], Output: ["e","l","l"]
    assert Solution.commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]

    # Unit Test: words = ["cool","lock","cook"], Output: ["c","o"]
    assert Solution.commonChars(["cool", "lock", "cook"]) == ["c", "o"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""1408. String Matching in an Array
Link: https://leetcode.com/problems/string-matching-in-an-array/
Difficulty: Easy
Description: Given an array of string words, return all strings in words that is a substring of
another word. You can return the answer in any order.
A substring is a contiguous sequence of characters within a string"""

from typing import List


class Solution:
    @staticmethod
    def stringMatching(words: List[str]) -> List[str]:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(n)."""
        substrings = []
        for i in range(len(words)):
            for j in range(len(words)):
                # If the word is a substring of another word
                if i != j and words[i] in words[j]:
                    substrings.append(words[i])
                    # Break the inner loop once the substring words[i] is found
                    break
        return substrings


# Unit Test: words = ["mass", "as", "hero", "superhero"], Output: ["as", "hero"]
assert Solution.stringMatching(["mass", "as", "hero", "superhero"]) == ["as", "hero"]

# Unit Test: words = ["leetcode", "et", "code"], Output: ["et", "code"]
assert Solution.stringMatching(["leetcode", "et", "code"]) == ["et", "code"]

# Unit Test: words = ["blue", "green", "bu"], Output: []
assert Solution.stringMatching(["blue", "green", "bu"]) == []

print("All unit tests are passed.")

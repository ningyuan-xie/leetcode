"""953. Verifying an Alien Dictionary
Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
Difficulty: Easy
Description: In an alien language, surprisingly, they also use English lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return
true if and only if the given words are sorted lexicographically in this alien language."""

from typing import List


class Solution:
    @staticmethod
    def isAlienSorted(words: List[str], order: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n*m), Space Complexity: O(1)"""
        # Initialize the hash table to store the order of each character in the alien language
        order_map = {char: i for i, char in enumerate(order)}

        def compare(word1: str, word2: str) -> bool:
            """Helper function to compare two words according to the alien dictionary order"""
            # Compare characters in both words: zip() will stop at min(len(word1), len(word2))
            for char1, char2 in zip(word1, word2):
                if order_map[char1] != order_map[char2]:
                    return order_map[char1] < order_map[char2]
            # If all characters are equal, the shorter word should come first
            return len(word1) <= len(word2)

        # Check if all adjacent words are in the correct order
        return all(compare(words[i], words[i + 1]) for i in range(len(words) - 1))


# Unit Test: Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz",
# Output: True
assert Solution.isAlienSorted(["hello", "leetcode"],
                              "hlabcdefgijkmnopqrstuvwxyz") is True

# Unit Test: Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz",
# Output: False
assert Solution.isAlienSorted(["word", "world", "row"],
                              "worldabcefghijkmnpqstuvxyz") is False

# Unit Test: Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz", Output: False
assert Solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") is False

# Unit Test: Inputs: words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx",
# "sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], order = "zkgwaverfimqxbnctdplsjyohu",
# Output: False
assert Solution.isAlienSorted(["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve",
                               "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge", "qmjwymmyox"],
                              "zkgwaverfimqxbnctdplsjyohu") is False

print("All unit tests are passed")

"""2273. Find Resultant Array After Removing Anagrams
Link: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
Difficulty: Easy
Description: You are given a 0-indexed string array words, where words[i] consists of lowercase
English letters.
In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i]
are anagrams, and delete words[i] from words. Keep performing this operation as long as you can
select an index that satisfies the conditions.
Return words after performing all operations. It can be shown that selecting the indices for each
operation in any arbitrary order will lead to the same result.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using
all the original letters exactly once. For example, "dacb" is an anagram of "abdc"."""

from typing import List


class Solution:
    @staticmethod
    def removeAnagrams(words: List[str]) -> List[str]:
        """Optimal Solution: Ignore the Anagrams. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the resultant list with the first word
        result = [words[0]]  # ["abba"]

        # Iterate through the list from the second word onward
        for i in range(1, len(words)):
            # Check if the current word is an anagram of the last added word
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])

        return result


# Unit Test: words = ["abba","baba","bbaa","cd","cd"], Output: ["abba","cd"]
assert Solution.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]) == ["abba", "cd"]

# Unit Test: words = ["a","b","c","d"], Output: ["a","b","c","d"]
assert Solution.removeAnagrams(["a", "b", "c", "d"]) == ["a", "b", "c", "d"]

# Unit Test: words = ["a","b","a"], Output: ["a","b","a"]
assert Solution.removeAnagrams(["a", "b", "a"]) == ["a", "b", "a"]

print("All unit tests are passed")

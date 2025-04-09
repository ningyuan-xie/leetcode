"""2085. Count Common Words With One Occurrence
Link: https://leetcode.com/problems/count-common-words-with-one-occurrence
Difficulty: Easy
Description: Given two string arrays words1 and words2, return the number of strings that appear
exactly once in each of the two arrays."""

from typing import List


class Solution:
    @staticmethod
    def countCommonWords(words1: List[str], words2: List[str]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Use dictionaries to store the frequencies of each word in the two words
        freq1, freq2 = {}, {}
        for w1 in words1:
            freq1[w1] = freq1.get(w1, 0) + 1
        for w2 in words2:
            freq2[w2] = freq2.get(w2, 0) + 1

        # Count the number of common words with one occurrence
        count = 0
        for w in set(words1).intersection(set(words2)):  # .instersection() finds the common words
            if freq1[w] == 1 and freq2[w] == 1:
                count += 1

        return count


# Unit Test: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"],
# Output: 2
assert Solution.countCommonWords(["leetcode", "is", "amazing", "as", "is"],
                                 ["amazing", "leetcode", "is"]) == 2

# Unit Test: words1 =["b","bb","bbb"], words2 = ["a","aa","aaa"], Output: 0
assert Solution.countCommonWords(["b", "bb", "bbb"], ["a", "aa", "aaa"]) == 0

print("All unit tests are passed.")

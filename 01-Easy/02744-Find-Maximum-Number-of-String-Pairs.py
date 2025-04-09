"""2744. Find Maximum Number of String Pairs
Link: https://leetcode.com/problems/find-maximum-number-of-string-pairs/
Difficulty: Easy
Description: You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:
- The string words[i] is equal to the reversed string of words[j].
- 0 <= i < j < words.length.
Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair."""

from typing import List


class Solution:
    @staticmethod
    def maximumNumberOfStringPairs(words: List[str]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the count and the hash map
        count = 0
        word_map = {}

        # Check each word: if its reversed version is in the hash map, pair them
        for word in words:
            reversed_word = word[::-1]
            # If the reversed word is in the hash map, pair it with the original word
            if reversed_word in word_map:
                count += 1
                word_map[reversed_word] -= 1
            # Otherwise, add the original word to the hash map
            else:
                word_map[word] = word_map.get(word, 0) + 1

        return count


# Unit Test: words = ["cd","ac","dc","ca","zz"], Output: 2
assert Solution.maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]) == 2

# Unit Test: words = ["ab","ba","cc"], Output: 1
assert Solution.maximumNumberOfStringPairs(["ab", "ba", "cc"]) == 1

# Unit Test: words = ["aa","ab"], Output: 0
assert Solution.maximumNumberOfStringPairs(["aa", "ab"]) == 0

print("All unit tests are passed.")

"""2399. Check Distances Between Same Letters
Link: https://leetcode.com/problems/check-distances-between-same-letters/
Difficulty: Easy
Description: You are given a 0-indexed string s consisting of only lowercase English letters, where
each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of
length 26.
Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
In a well-spaced string, the number of letters between the two occurrences of the ith letter is
distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.
Return true if s is a well-spaced string, otherwise return false."""

from typing import List


class Solution:
    @staticmethod
    def checkDistances(s: str, distance: List[int]) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)"""
        # Dictionary to store the first occurrence of each character
        first_occurrence = {}

        for (idx, char) in enumerate(s):
            if char in first_occurrence:  # s = "abaccb" -> first_occurrence = {'a': 0, 'b': 1, 'c': 3}
                # Calculate the actual distance between the two occurrences
                actual_distance = idx - first_occurrence[char] - 1
                expected_distance = distance[ord(char) - ord('a')]
                # distance[ord('b') - ord('a')] = distance[1] = 3

                if actual_distance != expected_distance:
                    return False
            else:
                # Store the first occurrence of the character
                first_occurrence[char] = idx

        return True


# Unit Test: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], Output: true
assert Solution.checkDistances("abaccb", [1, 3, 0, 5, 0, 0, 0, 0, 0, 0,
                                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) is True

# Unit Test: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], Output: false
assert Solution.checkDistances("aa",
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) is False

print("All unit tests are passed")

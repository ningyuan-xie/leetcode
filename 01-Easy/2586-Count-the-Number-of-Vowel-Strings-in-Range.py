"""2586. Count the Number of Vowel Strings in Range
Link: https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
Difficulty: Easy
Description: You are given a 0-indexed array of string words and two integers left and right.
A string is called a vowel string if it starts with a vowel character and ends with a vowel character
where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right]."""

from typing import List


class Solution:
    @staticmethod
    def vowelStrings(words: List[str], left: int, right: int) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)"""
        vowels = set("aeiou")
        count = 0

        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count


# Unit Test: words = ["are","amy","u"], left = 0, right = 2, Output: 2
assert Solution.vowelStrings(["are", "amy", "u"], 0, 2) == 2

# Unit Test: words = ["hey","aeo","mucoo","ooo","artro"], left = 1, right = 4, Output: 3
assert Solution.vowelStrings(["hey", "aeo", "mucoo", "ooo", "artro"], 1, 4) == 3

print("All unit tests are passed")

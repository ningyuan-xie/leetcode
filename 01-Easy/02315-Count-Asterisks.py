"""2315. Count Asterisks
Link: https://leetcode.com/problems/count-asterisks/
Difficulty: Easy
Description: You are given a string s, where every two consecutive vertical bars '|' are grouped into
a pair. In other words, the 1st '|' make a pair, the 2nd and 3th '|' make a pair, and so forth.
Return the number of '*' in s, excluding the '*' between each pair of '|'.
Note that each '|' will belong to exactly one pair."""


class Solution:
    @staticmethod
    def countAsterisks(s: str) -> int:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        asterisks = 0
        pair = False

        # 1st group considered; 2nd group ignored; 3rd group considered; 4th group ignored; and so on
        for char in s:
            if char == '|':
                pair = not pair
            elif char == '*' and pair is False:
                asterisks += 1

        return asterisks


# Unit Test: s = "l|*e*et|c**o|*de|", Output: 2
assert Solution.countAsterisks("l|*e*et|c**o|*de|") == 2

# Unit Test: s = "iamprogrammer", Output: 0
assert Solution.countAsterisks("iamprogrammer") == 0

# Unit Test: s = "yo|uar|e**|b|e***au|tifu|l", Output: 5
assert Solution.countAsterisks("yo|uar|e**|b|e***au|tifu|l") == 5

print("All unit tests are passed.")

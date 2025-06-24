"""2716. Minimize String Length
Link: https://leetcode.com/problems/minimize-string-length/
Difficulty: Easy
Description: Given a string s, you have two types of operation:
1. Choose an index i in the string, and let c be the character in position i. Delete the closest
occurrence of c to the left of i (if exists).
2. Choose an index i in the string, and let c be the character in position i. Delete the closest
occurrence of c to the right of i (if exists).
Your task is to minimize the length of s by performing the above operations zero or more times.
Return an integer denoting the length of the minimized string.g"""


class Solution:
    @staticmethod
    def minimizedStringLength(s: str) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)."""
        return len(set(s))


# Input: s = "aaabc", Output: 3
assert Solution.minimizedStringLength("aaabc") == 3

# Input: s = "cbbd", Output: 3
assert Solution.minimizedStringLength("cbbd") == 3

# Input: s = "baadccab", Output: 4
assert Solution.minimizedStringLength("baadccab") == 4

print("All unit tests are passed.")

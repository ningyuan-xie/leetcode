"""2351. First Letter to Appear Twice
Link: https://leetcode.com/problems/first-letter-to-appear-twice/
Difficulty: Easy
Description: Given a string s consisting of lowercase English letters, return the first letter to
appear twice.
Note:
- A letter a appears twice before another letter b if the second occurrence of a is before the
second occurrence of b.
- s will contain at least one letter that appears twice."""


class Solution:
    @staticmethod
    def firstLetterToAppearTwice(s: str) -> str:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)."""
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return ""

    @staticmethod
    def firstLetterToAppearTwiceDictionary(s: str) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        seen = {}
        for char in s:
            if char in seen:
                return char
            seen[char] = 1
        return ""


# Unit Test: s = "abccbaacz", Output: "c"
assert Solution.firstLetterToAppearTwice("abccbaacz") == "c"

# Unit Test: s = "abcdd", Output: "d"
assert Solution.firstLetterToAppearTwiceDictionary("abcdd") == "d"

print("All unit tests are passed.")

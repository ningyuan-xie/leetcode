"""1528. Shuffle String
Link: https://leetcode.com/problems/shuffle-string/
Difficulty: Easy
Description: You are given a string s and an integer array indices of the same length. The string s
will be shuffled such that the character at the ith position moves to indices[i] in the shuffled
string.
Return the shuffled string."""

from typing import List


class Solution:
    @staticmethod
    def restoreString(s: str, indices: List[int]) -> str:
        """Optimal Solution: List Manipulation. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the list to store the shuffled characters
        shuffled = [''] * len(s)

        # Iterate through the string and indices
        for (i, index) in enumerate(indices):  # (0, 4), (1, 5)
            # Place the character at the correct index
            shuffled[index] = s[i]  # shuffled[4] = s[0] = 'l', shuffled[5] = s[1] = 'e'

        # Join the shuffled characters into a single string
        return ''.join(shuffled)


# Unit Test: s = "codeleet", indices = [4, 5, 6, 7, 0, 2, 1, 3], Output: "leetcode"
assert Solution.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"

# Unit Test: s = "abc", indices = [0, 1, 2], Output: "abc"
assert Solution.restoreString("abc", [0, 1, 2]) == "abc"

# Unit Test: s = "aiohn", indices = [3, 1, 4, 2, 0], Output: "nihao"
assert Solution.restoreString("aiohn", [3, 1, 4, 2, 0]) == "nihao"

# Unit Test: s = "aaiougrt", indices = [4, 0, 2, 6, 7, 3, 1, 5], Output: "arigatou"
assert Solution.restoreString("aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5]) == "arigatou"

print("All unit tests are passed")

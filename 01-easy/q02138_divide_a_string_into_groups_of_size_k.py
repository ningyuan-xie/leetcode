"""2138. Divide a String Into Groups of Size k
Link: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k
Difficulty: Easy
Description: A string s can be partitioned into groups of size k using the following procedure:
- The first group consists of the first k characters of the string, the second group consists
of the next k characters of the string, and so on. Each character can be a part of exactly one group.
- For the last group, if the string does not have k characters remaining, a character fill is used
to complete the group.
Note that the partition is done so that after removing the fill character from the last group (if
it exists) and concatenating all the groups in order, the resultant string should be s.
Given the string s, the size of each group k and the character fill, return a string array denoting
the composition of every group s has been divided into, using the above procedure."""

from typing import List


class Solution:
    @staticmethod
    def divideString(s: str, k: int, fill: str) -> List[str]:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(s)
        # If the length of s is not divisible by k, fill the last group with fill
        if n % k != 0:
            return [s[i:i + k].ljust(k, fill)  # .ljust() fills the str with fill until it reaches len k
                    for i in range(0, n, k)]
        return [s[i:i + k]
                for i in range(0, n, k)]


# Input: s = "abcdefghi", k = 3, fill = "x", Output: ["abc","def","ghi"]
assert Solution.divideString("abcdefghi", 3, "x") == ["abc", "def", "ghi"]

# Input: ss = "abcdefghij", k = 3, fill = "x", Output: ["abc","def","ghi","jxx"]
assert Solution.divideString("abcdefghij", 3, "x") == ["abc", "def", "ghi", "jxx"]

print("All unit tests are passed.")

"""1876. Substrings of Size Three with Distinct Characters
Link: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
Difficulty: Easy
Description: A string is good if there are no repeated characters.
Given a string s, return the number of good substrings of length three in s.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string."""


class Solution:
    @staticmethod
    def countGoodSubstrings(s: str) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)."""
        count = 0

        for i in range(len(s) - 2):
            # Check if the current substring has distinct characters
            if len(set(s[i:i + 3])) == 3:
                count += 1

        return count


# Input: s = "xyzzaz", Output: 1
assert Solution.countGoodSubstrings("xyzzaz") == 1

# Input: s = "aababcabc", Output: 4
assert Solution.countGoodSubstrings("aababcabc") == 4

print("All unit tests are passed.")

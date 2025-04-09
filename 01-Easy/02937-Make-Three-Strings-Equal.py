"""2937. Make Three Strings Equal
Link: https://leetcode.com/problems/make-three-strings-equal/
Difficulty: Easy
Description: You are given three strings: s1, s2, and s3. In one operation you can choose one of
these strings and delete its rightmost character. Note that you cannot completely empty a string.
Return the minimum number of operations required to make the strings equal. If it is impossible
to make them equal, return -1."""


class Solution:
    @staticmethod
    def findMinimumOperations(s1: str, s2: str, s3: str) -> int:
        """Optimal Solution: Longest Common Prefix. Time Complexity: O(n), Space Complexity: O(1)"""
        # Find the minimum length of s1, s2, and s3
        n = min(len(s1), len(s2), len(s3))
        longest_common = 0

        # Find the longest common prefix of s1, s2, and s3
        for i in range(n):
            if s1[i] == s2[i] == s3[i]:
                longest_common += 1
            else:
                break

        return (len(s1) + len(s2) + len(s3) - 3 * longest_common) if longest_common > 0 else -1


# Unit Test: s1 = "abc", s2 = "abb", s3 = "ab", Output: 2
assert Solution.findMinimumOperations("abc", "abb", "ab") == 2

# Unit Test: s1 = "dac", s2 = "bac", s3 = "cac", Output: -1
assert Solution.findMinimumOperations("dac", "bac", "cac") == -1

# Unit Test: s1 = "a", s2 = "a", s3 = "a", Output: 0
assert Solution.findMinimumOperations("a", "a", "a") == 0

# Unit Test: s1 = "a", s2 = "aabc", s3 = "a", Output: 3
assert Solution.findMinimumOperations("a", "aabc", "a") == 3

print("All unit tests are passed.")

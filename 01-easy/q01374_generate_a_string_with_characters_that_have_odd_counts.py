"""1374. Generate a String With Characters That Have Odd Counts
Link: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
Difficulty: Easy
Description: Given an integer n, return a string with n characters such that each character in
such string occurs an odd number of times.
The returned string must contain only lowercase English letters. If there are multiples valid strings,
return any of them."""


class Solution:
    @staticmethod
    def generateTheString(n: int) -> str:
        """Optimal Solution: Construct the string with n-1 'a's and 1 'b' if n is even, otherwise
           construct the string with n 'a's.
           Time Complexity: O(n), Space Complexity: O(n)."""
        return "a" * (n - 1) + ("b" if n % 2 == 0 else "a")


# Unit Test: n = 4, Output: "aaab"
assert Solution.generateTheString(4) == "aaab"

# Unit Test: n = 2, Output: "ab"
assert Solution.generateTheString(2) == "ab"

# Unit Test: n = 7, Output: "aaaaaaa"
assert Solution.generateTheString(7) == "aaaaaaa"

print("All unit tests are passed.")

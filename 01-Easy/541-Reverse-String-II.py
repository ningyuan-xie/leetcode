"""541. Reverse String II
Link: https://leetcode.com/problems/reverse-string-ii/
Difficulty: Easy
Description: Given a string s and an integer k, reverse the first k characters for every 2k
characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and leave the other
as original."""


class Solution:
    @staticmethod
    def reverseStr(s: str, k: int) -> str:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0344-Reverse-String.py"""
        # Convert the string to a list of characters
        s = list(s)
        # Initialize the left and right pointers
        left, right = 0, 0
        # Loop until the right pointer reaches the end of the string
        while right < len(s):
            # Update both pointers
            left, right = right, min(right + k, len(s))
            # Reverse the first k characters
            # Remember that s[0:2] only picks the first 2 chars, while s[2] picks the 3rd char
            s[left:right] = s[left:right][::-1]
            # Skip the next k characters by moving the right pointer to the right by k
            right += k
        # Convert the list of characters back to a string
        return "".join(s)


# Unit Test: Input: s = "abcdefg", k = 2, Output: "bacdfeg"
assert Solution.reverseStr("abcdefg", 2) == "bacdfeg"

# Unit Test: Input: s = "abcd", k = 2, Output: "bacd"
assert Solution.reverseStr("abcd", 2) == "bacd"

print("All unit tests are passed")

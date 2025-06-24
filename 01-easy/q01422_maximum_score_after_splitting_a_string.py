"""1422. Maximum Score After Splitting a String
Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
Difficulty: Easy
Description: Given a string s of zeros and ones, return the maximum score after splitting the string
into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of
ones in the right substring."""


class Solution:
    @staticmethod
    def maxScore(s: str) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the count of zeros and ones in the string
        zeros = s[:1].count("0")  # s[:1] is the left substring (only the first char)
        ones = s[1:].count("1")  # s[1:] is the right substring (excluding the first char)

        # Initialize the max score
        max_score = zeros + ones

        # Iterate through the middle string to update zeros and ones:
        # Each loop, we assume left substring's len + 1, and right substring's len - 1
        for char in s[1:-1]:  # s[1:-1] is the middle part of the string
            # Increment zeros if the character is "0", since we allocate it to the left substring
            if char == "0":
                zeros += 1
            # Decrement ones if the character is "1", since we allocate it to the left substring
            else:
                ones -= 1
            max_score = max(max_score, zeros + ones)

        return max_score


# Input: s = "011101", Output: 5
assert Solution.maxScore("011101") == 5

# Input: s = "00111", Output: 5
assert Solution.maxScore("00111") == 5

# Input: s = "1111", Output: 3
assert Solution.maxScore("1111") == 3

# Input: s = "00", Output: 1
assert Solution.maxScore("00") == 1

print("All unit tests are passed.")

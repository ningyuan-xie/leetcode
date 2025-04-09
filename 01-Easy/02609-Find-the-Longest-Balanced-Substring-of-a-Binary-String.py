"""2609. Find the Longest Balanced Substring of a Binary String
Link: https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/
Difficulty: Easy
Description: You are given a binary string s consisting only of zeroes and ones.
A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is
equal to the number of ones inside the substring. Notice that the empty substring is considered a
balanced substring.
Return the length of the longest balanced substring of s.
A substring is a contiguous sequence of characters within a string."""


class Solution:
    @staticmethod
    def findTheLongestBalancedSubstring(s: str) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize variables to track the count of zeroes and ones
        max_length = 0
        i = 0
        n = len(s)

        while i < n:
            # Count consecutive 0s
            count_zeros = 0
            while i < n and s[i] == '0':
                count_zeros += 1
                i += 1

            # Count consecutive 1s
            count_ones = 0
            while i < n and s[i] == '1':
                count_ones += 1
                i += 1

            # Update max balanced length
            max_length = max(max_length, 2 * min(count_zeros, count_ones))

        return max_length


# Unit Test: s = "01000111", Output: 6
assert Solution.findTheLongestBalancedSubstring("01000111") == 6

# Unit Test: s = "00111", Output: 4
assert Solution.findTheLongestBalancedSubstring("00111") == 4

# Unit Test: s = "111", Output: 0
assert Solution.findTheLongestBalancedSubstring("111") == 0

# Unit Test: s = "", Output: 0
assert Solution.findTheLongestBalancedSubstring("") == 0

# Unit Test: s= "10", Output: 0
assert Solution.findTheLongestBalancedSubstring("10") == 0

print("All unit tests are passed.")

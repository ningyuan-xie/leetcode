"""696. Count Binary Substrings
Link: https://leetcode.com/problems/count-binary-substrings/
Difficulty: Easy
Description: Given a binary string s, return the number of non-empty substrings that have the same
number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur."""


class Solution:
    @staticmethod
    def countBinarySubstrings(s: str) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
           For a sequence like 0011, both 0 and 1 groups are of length 2. Thus, two valid substrings
           can be formed: 01 and 0011. Similarly, for 1100, the valid substrings are 10 and 1100"""
        # Initialize the count and the previous count
        count, prev_count = 0, 0
        # Initialize the two pointers
        start, end = 0, 0

        # Iterate through the string
        while start < len(s):
            # Count the number of consecutive 0's and 1's; stops whenever the character changes
            while end < len(s) and s[end] == s[start]:
                end += 1
            # Count the number of valid substrings, which is the minimal value between:
            # prev_count = length of the previous group; end - start = length of the current group
            count += min(prev_count, end - start)
            # Update the previous count (initially at 0)
            prev_count = end - start
            # Update the starting pointer and move on to the next group
            start = end

        return count


# Input: s = "00110011", Output: 6
# Explanation: There are 6 valid substrings: "0011", "01", "1100", "10", "0011", and "01"
assert Solution.countBinarySubstrings("00110011") == 6

# Input: s = "10101", Output: 4
# Explanation: There are 4 valid substrings: "10", "01", "10", and "01"
assert Solution.countBinarySubstrings("10101") == 4

print("All unit tests are passed.")

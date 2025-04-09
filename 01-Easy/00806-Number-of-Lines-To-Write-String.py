"""806. Number of Lines To Write String
Link: https://leetcode.com/problems/number-of-lines-to-write-string/
Difficulty: Easy
Description: You are given a string s of lowercase English letters and an array widths denoting
how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of
'a', widths[1] is the width of 'b', and so on.
You are trying to write s across several lines, where each line is no longer than 100 pixels.
Starting at the beginning of s, write as many letters on the first line such that the total width
does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters
as you can on the second line. Continue this process until you have written all of s.
Return an array result of length 2 where:
result[0] is the total number of lines.
result[1] is the width of the last line in pixels."""

from typing import List


class Solution:
    @staticmethod
    def numberOfLines(widths: List[int], s: str) -> List[int]:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1).
           Linear Scan: Iterate exactly once through the string s and calculate the number of lines"""
        # Initialize the number of lines and the width of the current line
        num_lines = 1
        line_width = 0

        for char in s:
            # Calculate the width of the current character
            char_width = widths[ord(char) - ord('a')]
            # If the current line width exceeds 100,
            # increment the number of lines and reset the line width
            if line_width + char_width > 100:
                num_lines += 1
                line_width = 0
            # Update the line width
            line_width += char_width

        return [num_lines, line_width]


# Unit Test:
# Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
# s = "abcdefghijklmnopqrstuvwxyz"
assert Solution.numberOfLines(
    [10, 10, 10, 10, 10,
     10, 10, 10, 10, 10,
     10, 10, 10, 10, 10,
     10, 10, 10, 10, 10,
     10, 10, 10, 10, 10, 10],
    "abcdefghijklmnopqrstuvwxyz") == [3, 60]  # 100 + 100 + 60 pixels wide

# Unit Test:
# Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
# s = "bbbcccdddaaa"
assert Solution.numberOfLines(
    [4, 10, 10, 10, 10,
     10, 10, 10, 10, 10,
     10, 10, 10, 10, 10,
     10, 10, 10, 10, 10,
     10, 10, 10, 10, 10, 10],
    "bbbcccdddaaa") == [2, 4]  # 98 + 4 pixels wide

print("All unit tests are passed.")

"""806. Number of Lines To Write String
Link: https://leetcode.com/problems/number-of-lines-to-write-string/
Difficulty: Easy
Description: You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.
You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.
Return an array result of length 2 where:
• result[0] is the total number of lines.
• result[1] is the width of the last line in pixels."""

from typing import List


class Solution:
    @staticmethod
    def numberOfLines(widths: List[int], s: str) -> List[int]:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        lines, width = 1, 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            width += w
            # If the current line width exceeds 100, increment the number of lines and reset the line width
            if width > 100:
                lines += 1
                width = w
        return [lines, width]


def unit_tests():
    # Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
    assert Solution.numberOfLines([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "abcdefghijklmnopqrstuvwxyz") == [3, 60]

    # Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
    assert Solution.numberOfLines([4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "bbbcccdddaaa") == [2, 4]


if __name__ == '__main__':
    unit_tests()
    print("All unit tests are passed.")

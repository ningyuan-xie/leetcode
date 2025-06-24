"""3206. Alternating Groups I
Link: https://leetcode.com/problems/alternating-groups-i
Difficulty: Easy
Description: There is a circle of red and blue tiles. You are given an array of integers colors.
The color of tile i is represented by colors[i]:
- colors[i] == 0 means that tile i is red.
- colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different
color from its left and right tiles) is called an alternating group.
Return the number of alternating groups.
Note that since colors represents a circle, the first and the last tiles are considered to be
next to each other."""

from typing import List


class Solution:
    @staticmethod
    def numberOfAlternatingGroups(colors: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        count = 0
        n = len(colors)
        for i in range(n):
            if colors[i] != colors[(i + 1) % n] and colors[i] != colors[(i - 1) % n]:
                count += 1

        return count


# Input: colors = [1,1,1], Output = 0
assert Solution.numberOfAlternatingGroups([1, 1, 1]) == 0

# Input: colors = [0,1,0,0,1], Output = 3
assert Solution.numberOfAlternatingGroups([0, 1, 0, 0, 1]) == 3

print("All unit tests are passed.")

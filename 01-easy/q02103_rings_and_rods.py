"""2103. Rings and Rods
Link: https://leetcode.com/problems/rings-and-rods
Difficulty: Easy
Description: There are n rings and each ring is either red, green, or blue. The rings are
distributed across ten rods labeled from 0 to 9.
You are given a string rings of length 2n that describes the n rings that are placed onto the rods.
Every two characters in rings forms a color-position pair that is used to describe each ring where:
- The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
- The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring
placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.
Return the number of rods that have all three colors of rings on them."""

from typing import List


class Solution:
    @staticmethod
    def countPoints(rings: str) -> int:
        """Optimal Solution: Hash Table & Set. Time Complexity: O(n), Space Complexity: O(1)."""
        # Dictionary to store colors for each rod; colors are stored in a set to avoid duplicates
        rod_colors = {str(i): set() for i in range(10)}  # {'0': set(), '1': set(), ..., '9': set()}

        # Step through the string in pairs
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]
            rod_colors[rod].add(color)  # {'0': {'R'}, '1': {'B'}, '2': {'G'}, '3': {'R'}, ...}

        # Count rods with all three colors
        count = sum(1 for colors in rod_colors.values()
                    if {'R', 'G', 'B'}.issubset(colors))
        return count


# Unit Test: rings = "B0B6G0R6R0R6G9", Output: 1
assert Solution.countPoints("B0B6G0R6R0R6G9") == 1

# Unit Test: rings = "B0R0G0R9R0B0G0", Output: 1
assert Solution.countPoints("B0R0G0R9R0B0G0") == 1

# Unit Test: rings = "G4", Output: 0
assert Solution.countPoints("G4") == 0

print("All unit tests are passed.")

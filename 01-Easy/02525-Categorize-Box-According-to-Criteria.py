"""2525. Categorize Box According to Criteria
Link: https://leetcode.com/problems/categorize-box-according-to-criteria/
Difficulty: Easy
Description: Given four integers length, width, height, and mass, representing the dimensions and mass
of a box, respectively, return a string representing the category of the box.
- The box is "Bulky" if:
-- Any of the dimensions of the box is greater or equal to 10^4.
-- Or, the volume of the box is greater or equal to 10^9.
- If the mass of the box is greater or equal to 100, it is "Heavy".
- If the box is both "Bulky" and "Heavy", then its category is "Both".
- If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
- If the box is "Bulky" but not "Heavy", then its category is "Bulky".
- If the box is "Heavy" but not "Bulky", then its category is "Heavy".
Note that the volume of the box is the product of its length, width and height."""

from typing import List


class Solution:
    @staticmethod
    def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
        """Optimal Solution: If-Else. Time Complexity: O(1), Space Complexity: O(1)"""
        # Initialize bulky and heavy to False
        bulky, heavy = False, False

        if (length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4
                or length * width * height >= 10 ** 9):
            bulky = True
        if mass >= 100:
            heavy = True
        if bulky and heavy:
            return "Both"
        elif not bulky and not heavy:
            return "Neither"
        elif bulky and not heavy:
            return "Bulky"
        elif not bulky and heavy:
            return "Heavy"


# Input: length = 1000, width = 35, height = 700, mass = 300, Output: "Heavy"
assert Solution.categorizeBox(1000, 35, 700, 300) == "Heavy"

# Input: length = 200, width = 50, height = 800, mass = 50, Output: "Neither"
assert Solution.categorizeBox(200, 50, 800, 50) == "Neither"

print("All unit tests are passed.")

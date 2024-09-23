"""1232. Check If It Is a Straight Line
Link: https://leetcode.com/problems/check-if-it-is-a-straight-line
Difficulty: Easy
Description: You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
represents the coordinate of a point.
Check if these points make a straight line in the XY plane."""

from typing import List


class Solution:
    @staticmethod
    def checkStraightLine(coordinates: List[List[int]]) -> bool:
        """Optimal Solution: Slope Calculation. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 1037-Valid-Boomerang.py"""
        # Calculate the slope of the line between the first two points
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        slope = (y1 - y0) / (x1 - x0) if x1 - x0 != 0 else float('inf')

        # Check if the slope between the rest of the points is the same as the initial slope
        for i in range(2, len(coordinates)):
            x0, y0 = coordinates[i - 1]
            x1, y1 = coordinates[i]
            new_slope = (y1 - y0) / (x1 - x0) if x1 - x0 != 0 else float('inf')
            if new_slope != slope:
                return False

        return True


# Unit Test: coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], Output: True
assert Solution.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) is True

# Unit Test: coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], Output: False
assert Solution.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) is False

# Unit Test: coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], Output: True
assert Solution.checkStraightLine([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) is True

print("All unit tests are passed")

"""1037. Valid Boomerang
Link: https://leetcode.com/problems/valid-boomerang/
Difficulty: Easy
Description: Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
A boomerang is a set of three points that are all distinct and not in a straight line."""

from typing import List


class Solution:
    @staticmethod
    def isBoomerang(points: List[List[int]]) -> bool:
        """Optimal Solution: Slope Calculation. Time Complexity: O(1), Space Complexity: O(1)."""
        # Ensure that no two points are identical
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False

        # Calculate the slope of the first two points
        slope1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) if points[1][0] != points[0][0] else float("inf")

        # Calculate the slope of the first and third points
        slope2 = (points[2][1] - points[0][1]) / (points[2][0] - points[0][0]) if points[2][0] != points[0][0] else float("inf")

        # Return True if the slopes are different, meaning the points are not collinear
        return slope1 != slope2


def unit_tests():
    # Input: points = [[1, 1], [2, 3], [3, 2]], Output: True
    assert Solution.isBoomerang([[1, 1], [2, 3], [3, 2]]) is True

    # Input: points = [[1, 1], [2, 2], [3, 3]], Output: False
    assert Solution.isBoomerang([[1, 1], [2, 2], [3, 3]]) is False

    # Input: points = [[1, 1], [2, 2], [1, 1]], Output: False
    assert Solution.isBoomerang([[1, 1], [2, 2], [1, 1]]) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

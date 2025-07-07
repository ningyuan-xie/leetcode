"""1266. Minimum Time Visiting All Points
Link: https://leetcode.com/problems/minimum-time-visiting-all-points/
Difficulty: Easy
Description: On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.
You can move according to these rules:
• In 1 second, you can either:
  • move vertically by one unit,
  • move horizontally by one unit, or
  • move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
• You have to visit the points in the same order as they appear in the array.
• You are allowed to pass through points that appear later in the order, but these do not count as visits."""

from typing import List


class Solution:
    @staticmethod
    def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
        """Optimal Solution: Greedy Approach. Time Complexity: O(n), Space Complexity: O(1)."""
        total_time = 0

        # Calculate the time to move from one point to the next
        for i in range(len(points) - 1):
            # Calculate the distance between two points
            x0, y0 = points[i]
            x1, y1 = points[i + 1]
            dx, dy = abs(x1 - x0), abs(y1 - y0)

            # Greedy Approach: Move diagonally as much as possible
            diagonal_distance = min(dx, dy)
            remaining_distance = abs(dx - dy)

            # Calculate the total time to move from one point to the next
            total_time += diagonal_distance + remaining_distance

        return total_time


def unit_tests():
    # Input: points = [[1, 1], [3, 4], [-1, 0]], Output: 7
    # One optimal path is: [1, 1] -> [2, 2] -> [3, 3] -> [3, 4] -> [2, 3] -> [1, 2] -> [0, 1] -> [-1, 0]
    assert Solution.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]) == 7

    # Input: points = [[3, 2], [-2, 2]], Output: 5
    # One optimal path is: [3, 2] -> [2, 2] -> [1, 2] -> [0, 2] -> [-1, 2] -> [-2, 2]
    assert Solution.minTimeToVisitAllPoints([[3, 2], [-2, 2]]) == 5


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

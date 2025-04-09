"""1732. Find the Highest Altitude
Link: https://leetcode.com/problems/find-the-highest-altitude/
Difficulty: Easy
Description: There is a biker going on a road trip. The road trip consists of n + 1 points at
different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between
points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point."""


from typing import List


class Solution:
    @staticmethod
    def largest_altitude(gain: List[int]) -> int:
        """Optimal Solution: Cumulative Sum. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the highest altitude and the current altitude
        highest_altitude = current_altitude = 0

        # Calculate the highest altitude
        for altitude in gain:
            current_altitude += altitude
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude


# Unit Test: gain = [-5, 1, 5, 0, -7], Output: 1
assert Solution.largest_altitude([-5, 1, 5, 0, -7]) == 1

# Unit Test: gain = [-4, -3, -2, -1, 4, 3, 2], Output: 0
assert Solution.largest_altitude([-4, -3, -2, -1, 4, 3, 2]) == 0

# Unit Test: gain = [1, 2, 3, 4, 5], Output: 15
assert Solution.largest_altitude([1, 2, 3, 4, 5]) == 15

print("All unit tests are passed.")

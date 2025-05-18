"""495. Teemo Attacking
Link: https://leetcode.com/problems/teemo-attacking/
Difficulty: Easy
Description: Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.
You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.
Return the total number of seconds that Ashe is poisoned."""

from typing import List


class Solution:
    @staticmethod
    def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the total poisoned duration
        total_duration = 0

        # Iterate through the time series
        for i in range(len(timeSeries) - 1):
            # Calculate the time difference between consecutive attacks
            time_diff = timeSeries[i + 1] - timeSeries[i]

            # If the time difference is less than the duration, add it to the total duration
            if time_diff < duration:
                total_duration += time_diff
            else:
                # If the time difference is greater than or equal to the duration, add the full duration
                total_duration += duration

        # Add the duration of the last attack
        total_duration += duration

        return total_duration


def unit_tests():
    # Input: time_series = [1, 4], duration = 2, Output: 4
    assert Solution.findPoisonedDuration([1, 4], 2) == 4

    # Input: time_series = [1, 2], duration = 2, Output: 3
    assert Solution.findPoisonedDuration([1, 2], 2) == 3

    # Input: time_series = [1, 2, 5, 10], duration = 3, Output: 10
    assert Solution.findPoisonedDuration([1, 2, 5, 10], 3) == 10


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

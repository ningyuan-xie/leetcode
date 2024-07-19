# Link: https://leetcode.com/problems/teemo-attacking/
# Difficulty: Easy
# Our hero Teemo is attacking an enemy Ashe with poison attacks!
# When Teemo attacks Ashe, Ashe gets poisoned for an exact duration seconds.
# More formally, an attack at second t will mean Ashe is poisoned during the
# inclusive time interval [t, t + duration - 1].
# If Teemo attacks again before the poison effect ends, the timer for it is reset,
# and the poison effect will end duration seconds after the new attack.
# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that
# Teemo attacks Ashe at second timeSeries[i], and an integer duration.
# Return the total number of seconds that Ashe is poisoned.

from typing import List


class Solution:
    # Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)
    # Similar to 0121-Best-Time-to-Buy-and-Sell-Stock.py
    @staticmethod
    def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
        # Base Case: If the time series is empty, return 0
        if not timeSeries:
            return 0
        total_poisoned_duration = 0
        # Iterate through each current attack and its previous attack at timeSeries[i - 1]
        for i in range(1, len(timeSeries)):
            # Calculate the poisoned duration between two attacks, which is the min of:
            # 1. The time between the current and previous attacks (as attacks will reset the dot)
            # 2. The duration of the poison
            total_poisoned_duration += min(timeSeries[i] - timeSeries[i - 1], duration)
        # Add the last current attack's poisoned duration at timeSeries[i]
        total_poisoned_duration += duration
        return total_poisoned_duration


# Unit Test: Input: time_series = [1, 4], duration = 2, Output: 4
# Poisoned Duration: attacks at 1 -> [1, 2] -> attacks at 4 -> [4, 5] -> 4 seconds
assert Solution.findPoisonedDuration([1, 4], 2) == 4

# Unit Test: Input: time_series = [1, 2], duration = 2, Output: 3
# Poisoned Duration: attacks at 1 -> [1, 2] -> attacks at 2 -> [2, 3] -> 3 seconds
assert Solution.findPoisonedDuration([1, 2], 2) == 3

# Unit Test: Input: time_series = [1, 2, 5, 10], duration = 3, Output: 10
# Poisoned Duration: attacks at 1 -> [1, 2, 3] -> attacks at 2 -> [2, 3, 4] ->
# attacks at 5 -> [5, 6, 7] -> attacks at 10 -> [10, 11, 12] -> 10 seconds
assert Solution.findPoisonedDuration([1, 2, 5, 10], 3) == 10

print("All unit tests are passed")

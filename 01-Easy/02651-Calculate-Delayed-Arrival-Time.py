"""2651. Calculate Delayed Arrival Time
Link: https://leetcode.com/problems/calculate-delayed-arrival-time/
Difficulty: Easy
Description: You are given a positive integer arrivalTime denoting the arrival time of a train in
hours, and another positive integer delayedTime denoting the amount of delay in hours.
Return the time when the train will arrive at the station.
Note that the time in this problem is in 24-hours format."""


class Solution:
    @staticmethod
    def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)"""
        return (arrivalTime + delayedTime) % 24


# Unit Test: arrivalTime = 15, delayedTime = 5, Output: 20
assert Solution.findDelayedArrivalTime(15, 5) == 20

# Unit Test: arrivalTime = 13, delayedTime = 11, Output: 0
assert Solution.findDelayedArrivalTime(13, 11) == 0

print("All unit tests are passed.")

"""1184. Distance Between Bus Stops
Link: https://leetcode.com/problems/distance-between-bus-stops/
Difficulty: Easy
Description: A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance
between all pairs of neighboring stops where distance[i] is the distance between the stops
number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops."""

from typing import List


class Solution:
    @staticmethod
    def distanceBetweenBusStops(distance: List[int], start: int, destination: int) -> int:
        """Optimal Solution: Calculate the total distance and the clockwise distance.
           Time Complexity: O(n), Space Complexity: O(1)."""
        # Calculate the total distance
        total_distance = sum(distance)  # 1 + 2 + 3 + 4 = 10

        # Calculate the clockwise distance
        clockwise_distance = sum(distance[min(start, destination):  # min(0, 1) = 0
                                          max(start, destination)])  # max(0, 1) = 1

        # Calculate the counterclockwise distance
        counterclockwise_distance = total_distance - clockwise_distance  # 10 - 1 = 9

        return min(clockwise_distance, counterclockwise_distance)  # min(1, 9) = 1


# Input: distance = [1, 2, 3, 4], start = 0, destination = 1, Output: 1
assert Solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 1) == 1

# Input: distance = [1, 2, 3, 4], start = 0, destination = 2, Output: 3
assert Solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 2) == 3

# Input: distance = [1, 2, 3, 4], start = 0, destination = 3, Output: 4
assert Solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 3) == 4

print("All unit tests are passed.")

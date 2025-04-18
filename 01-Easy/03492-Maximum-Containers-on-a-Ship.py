"""3492. Maximum Containers on a Ship
Link: https://leetcode.com/problems/maximum-containers-on-a-ship/
Difficulty: Easy
Description: You are given a positive integer n representing an n x n cargo deck on a ship. Each cell on the deck can hold one container with a weight of exactly w.
However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, maxWeight.
Return the maximum number of containers that can be loaded onto the ship."""

from typing import List


class Solution:
    @staticmethod
    def maxContainers(n: int, w: int, maxWeight: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        # Calculate the maximum number of containers that can be loaded
        max_containers = min(n * n, maxWeight // w)
        return max_containers


def unit_tests():
    # Input: n = 2, w = 3, maxWeight = 15, Output: 4
    assert Solution.maxContainers(2, 3, 15) == 4

    # Input: n = 3, w = 5, maxWeight = 20, Output: 4
    assert Solution.maxContainers(3, 5, 20) == 4


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

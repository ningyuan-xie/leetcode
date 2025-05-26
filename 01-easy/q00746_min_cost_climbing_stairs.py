"""746. Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Difficulty: Easy
Description: You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor."""

from typing import List


class Solution:
    @staticmethod
    def min_cost_climbing_stairs(cost: List[int]) -> int:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(1).
        Similar to 70. Climbing Stairs."""
        # Initialize dp variables for first two steps
        first_cost, second_cost = cost[0], cost[1]
        
        # Iterate from step 2 to end
        for i in range(2, len(cost)):
            # Current step's cost is cost[i] plus minimum of previous two steps
            current = cost[i] + min(first_cost, second_cost)
            # Update previous two steps for next iteration
            first_cost, second_cost = second_cost, current
            
        # Final result is minimum of last two steps since we can reach top from either
        return min(first_cost, second_cost)


def unit_tests():
    # Input: cost = [10, 15, 20], Output: 15
    assert Solution.min_cost_climbing_stairs([10, 15, 20]) == 15

    # Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], Output: 6
    assert Solution.min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

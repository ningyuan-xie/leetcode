"""746. Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Difficulty: Easy
Description: You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps. You can either start from the step with
index 0 or the step with index 1. Return the minimum cost to reach the top of the floor."""

from typing import List


class Solution:
    @staticmethod
    def min_cost_climbing_stairs(cost: List[int]) -> int:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0070-Climbing-Stairs.py, but this question assumes the beginning is already
           at a step (not ground), and after the last step there is a top"""
        # Initialization: Assume we are standing at 2nd step cost[1], which is the current step
        # first_cost = the minimum cost to climb from the step before the current step;
        # second_cost = the minimum cost to climb from the current step
        first_cost, second_cost = cost[0], cost[1]

        # Analyze each remaining step one by one: each step has two ways to reach
        for i in range(2, len(cost)):
            # There are two ways to reach the current step, so pick the one with lesser cumulative cost
            current_cost = min(first_cost, second_cost) + cost[i]

            # Update: Assume we are standing at the next step
            first_cost, second_cost = second_cost, current_cost

        # After the iteration: we are standing at the last step; there is a top afterward
        # first_cost = the cumulative cost to climb from the step before the last step;
        # second_cost = the cumulative cost to climb from the last step
        return min(first_cost, second_cost)


# Input: cost = [10, 15, 20], Output: 15
assert Solution.min_cost_climbing_stairs([10, 15, 20]) == 15

# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], Output: 6
assert Solution.min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

print("All unit tests are passed.")

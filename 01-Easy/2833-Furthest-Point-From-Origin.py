"""2833. Furthest Point From Origin
Link: https://leetcode.com/problems/furthest-point-from-origin/
Difficulty: Easy
Description: You are given a string moves of length n consisting only of characters 'L', 'R',
and '_'. The string represents your movement on a number line starting from the origin 0.
In the ith move, you can choose one of the following directions:
- move to the left if moves[i] = 'L' or moves[i] = '_'
- move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves."""

from typing import List


class Solution:
    @staticmethod
    def furthestDistanceFromOrigin(moves: str) -> int:
        """Optimal Solution: Count L and R Moves. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the count of L and R moves
        count_L, count_R = 0, 0
        count__ = moves.count('_')

        # Compare L and R moves
        for move in moves:
            if move == 'L':
                count_L += 1
            elif move == 'R':
                count_R += 1

        # Return the absolute difference between L and R moves plus the count of _
        return abs(count_L - count_R) + count__


# Unit Test: moves = "L_RL__R", Output: 3
assert Solution.furthestDistanceFromOrigin("L_RL__R") == 3

# Unit Test: moves = "_R__LL_", Output: 5
assert Solution.furthestDistanceFromOrigin("_R__LL_") == 5

# Unit Test: moves = "_______", Output: 7
assert Solution.furthestDistanceFromOrigin("_______") == 7

print("All unit tests are passed")

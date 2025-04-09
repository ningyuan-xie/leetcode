"""2511. Maximum Enemy Forts That Can Be Captured
Link: https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/
Difficulty: Easy
Description: You are given a 0-indexed integer array forts of length n representing the positions of
several forts. forts[i] can be -1, 0, or 1 where:
- -1 represents there is no fort at the ith position.
- 0 indicates there is an enemy fort at the ith position.
- 1 indicates the fort at the ith the position is under your command.
Now you have decided to move your army from one of your forts at position i to an empty position j
such that:
- 0 <= i, j <= n - 1
- The army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j), forts[k] == 0.
While moving the army, all the enemy forts that come in the way are captured.
Return the maximum number of enemy forts that can be captured. In case it is impossible to move your
army, or you do not have any fort under your command, return 0."""

from typing import List


class Solution:
    @staticmethod
    def captureForts(forts: List[int]) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
           Traverse the array, track the last non-zero fort (1 or -1), and calculate captured enemy
           forts (0s) between valid fort pairs (1 and -1)."""
        max_captured = 0
        n = len(forts)
        prev = -1  # no fort seen yet

        for i in range(n):
            if forts[i] == 0:  # Skip the enemy forts
                continue

            # When we reach a point where (start, end) are (1, -1) or (-1, 1), record the forts passed
            if prev != -1 and forts[prev] + forts[i] == 0:  # Valid two end points: 1 and -1
                max_captured = max(max_captured, abs(i - prev) - 1)

            # Record the current fort, whenever we see a 1 or -1
            prev = i

        return max_captured


# Unit Test: forts = [1,0,0,-1,0,0,0,0,1], Output: 4
assert Solution.captureForts([1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4

# Unit Test: forts = [0,0,1,-1], Output: 0
assert Solution.captureForts([0, 0, 1, -1]) == 0

print("All unit tests are passed.")

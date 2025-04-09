"""2923. Find Champion I
Link: https://leetcode.com/problems/find-champion-i/
Difficulty: Easy
Description: There are n teams numbered from 0 to n - 1 in a tournament.
Given a 0-indexed 2D boolean matrix grid of size n * n. For all i, j that 0 <= i, j <= n - 1
and i != j team i is stronger than team j if grid[i][j] == 1, otherwise, team j is stronger
than team i.
Team a will be the champion of the tournament if there is no team b that is stronger than team a.
Return the team that will be the champion of the tournament."""

from typing import List


class Solution:
    @staticmethod
    def findChampion(grid: List[List[int]]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n^2), Space Complexity: O(n)"""
        n = len(grid)
        teams = {}

        # Count the number of 1s in each team
        for i in range(n):
            teams[i] = grid[i].count(1)

        return max(teams, key=teams.get)


# Unit Test: grid = [[0,1],[0,0]], Output: 0
assert Solution.findChampion([[0, 1], [0, 0]]) == 0

# Unit Test: grid = [[0,0,1],[1,0,1],[0,0,0]], Output: 1
assert Solution.findChampion([[0, 0, 1], [1, 0, 1], [0, 0, 0]]) == 1

print("All unit tests are passed")

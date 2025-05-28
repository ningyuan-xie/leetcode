"""3402. Minimum Operations to Make Columns Strictly Increasing
Link: https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/
Difficulty: Easy
Description: You are given a m x n matrix grid consisting of non-negative integers.
In one operation, you can increment the value of any grid[i][j] by 1.
Return the minimum number of operations needed to make all columns of grid strictly increasing."""

from typing import List


class Solution:
    @staticmethod
    def minimumOperations(grid: List[List[int]]) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(m*n), Space Complexity: O(1)."""
        m, n = len(grid), len(grid[0])
        operations = 0

        # Traverse the grid column-wise
        for j in range(n):
            for i in range(1, m):
                if grid[i][j] <= grid[i - 1][j]:
                    operations += grid[i - 1][j] - grid[i][j] + 1
                    grid[i][j] += grid[i - 1][j] - grid[i][j] + 1

        return operations


def unit_tests():
    # Input: grid = [[3,2],[1,3],[3,4],[0,1]], Output: 15
    assert Solution.minimumOperations([[3, 2], [1, 3], [3, 4], [0, 1]]) == 15

    # Input: grid = [[3,2,1],[2,1,0],[1,2,3]], Output: 12
    assert Solution.minimumOperations([[3, 2, 1], [2, 1, 0], [1, 2, 3]]) == 12


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

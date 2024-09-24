"""1260. Shift 2D Grid
Link: https://leetcode.com/problems/shift-2d-grid/
Difficulty: Easy
Description: Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
In one shift operation:
Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times."""

from typing import List


class Solution:
    @staticmethod
    def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
        """Optimal Solution: 1D List and Modulo Operation.
           Time Complexity: O(m * n), Space Complexity: O(m * n)"""
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Flatten the grid into a 1D list
        flat_grid = [grid[i][j] for i in range(m) for j in range(n)]

        # Since shifting the grid m * n times results in the same grid, the effective number of shifts
        # needed is k % (m * n)
        k %= m * n

        # Perform the shift
        flat_grid = (flat_grid[-k:]  # the last k elements
                     + flat_grid[:-k])  # the remaining elements from the start up to the last k

        # Reshape the 1D list back to a 2D grid: grid[i][j] = flat_grid[i * n + j]
        for i in range(m):  # E.g. m = 3: i = 0, 1, 2
            for j in range(n):  # E.g. n = 3: j = 0, 1, 2
                grid[i][j] = flat_grid[i * n + j]  # E.g. grid[1][2] = flat_grid[1 * 3 + 2] = flat_grid[5]
        return grid


# Unit Test: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 1,
# Output: [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
assert (Solution.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
        == [[9, 1, 2], [3, 4, 5], [6, 7, 8]])

# Unit Test: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4,
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
assert (Solution.shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4)
        == [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]])

print("All unit tests are passed")

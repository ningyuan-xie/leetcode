"""3417. Zigzag Grid Traversal With Skip
Link: https://leetcode.com/problems/zigzag-grid-traversal-with-skip/
Difficulty: Easy
Description: You are given an m x n 2D array grid of positive integers.
Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.
Zigzag pattern traversal is defined as following the below actions:
• Start at the top-left cell (0, 0).
• Move right within a row until the end of the row is reached.
• Drop down to the next row, then traverse left until the beginning of the row is reached.
• Continue alternating between right and left traversal until every row has been traversed.
Note that you must skip every alternate cell during the traversal.
Return an array of integers result containing, in order, the value of the cells visited during the zigzag traversal with skips."""

from typing import List


class Solution:
    @staticmethod
    def zigzagTraversal(grid: List[List[int]]) -> List[int]:
        """Optimal Solution: Matrix Traversal. Time Complexity: O(m * n), Space Complexity: O(1)."""
        m, n = len(grid), len(grid[0])
        result = []

        for i in range(m):
            if i % 2 == 0:
                # Traverse right
                for j in range(0, n, 2):
                    result.append(grid[i][j])
            else:
                # Traverse left
                if n % 2 == 0:
                    # If n is even, start from the last column
                    for j in range(n - 1, -1, -2):
                        result.append(grid[i][j])
                else:
                    # If n is odd, start from the second last column
                    for j in range(n - 2, -1, -2):
                        result.append(grid[i][j])
        return result


def unit_tests():
    # Input: grid = [[1,2],[3,4]], Output: [1,4]
    assert Solution.zigzagTraversal([[1, 2], [3, 4]]) == [1, 4]

    # Input: grid = [[2,1],[2,1],[2,1]], Output: [2,1,2]
    assert Solution.zigzagTraversal([[2, 1], [2, 1], [2, 1]]) == [2, 1, 2]

    # Input: grid = [[1,2,3],[4,5,6],[7,8,9]], Output: [1,3,5,7,9]
    assert Solution.zigzagTraversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 3, 5, 7, 9]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""2500. Delete Greatest Value in Each Row
Link: https://leetcode.com/problems/delete-greatest-value-in-each-row/
Difficulty: Easy
Description: You are given an m x n matrix grid consisting of positive integers.
Perform the following operation until grid becomes empty:
- Delete the element with the greatest value from each row. If multiple such elements exist, delete
any of them.
- Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.
Return the answer after performing the operations described above."""

from typing import List


class Solution:
    @staticmethod
    def deleteGreatestValue(grid: list[list[int]]) -> int:
        """Optimal Solution: Sorting. Time Complexity: O(m * n * log(n)), Space Complexity: O(1)"""
        # Sort each row in descending order
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
        # E.g. [[1, 2, 4], [3, 3, 1]] -> [[4, 2, 1], [3, 3, 1]]

        # Initialize the answer to 0
        ans = 0

        # Iterate through each column
        for j in range(len(grid[0])):
            # Find the maximum value in the current column
            max_value = max([grid[i][j] for i in range(len(grid))])  # 4, 3, 1
            # Add the maximum value to the answer
            ans += max_value

        return ans


# Unit Test: grid = [[1, 2, 4], [3, 3, 1]], Output: 8
assert Solution.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]) == 8

# Unit Test: grid = [[10]], Output: 10
assert Solution.deleteGreatestValue([[10]]) == 10

print("All unit tests are passed.")

"""1380. Lucky Numbers in a Matrix
Link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
Difficulty: Easy
Description: Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any
order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum
in its column."""

from typing import List


class Solution:
    @staticmethod
    def luckyNumbers(matrix: List[List[int]]) -> List[int]:
        """Optimal Solution: Brute Force. Time Complexity: O(m*n), Space Complexity: O(1)."""
        lucky_numbers = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == min(matrix[i])  # min in row
                        == max(matrix[k][j] for k in range(len(matrix)))):  # max in column
                    lucky_numbers.append(matrix[i][j])
        return lucky_numbers


# Input: matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]], Output: [15]
assert Solution.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]) == [15]

# Input: matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], Output: [12]
assert Solution.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]) == [12]

# Input: matrix = [[7, 8], [1, 2]], Output: [7]
assert Solution.luckyNumbers([[7, 8], [1, 2]]) == [7]

print("All unit tests are passed.")

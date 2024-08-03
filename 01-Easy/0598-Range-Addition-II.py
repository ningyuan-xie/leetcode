"""598. Range Addition II
Link: https://leetcode.com/problems/range-addition-ii/
Difficulty: Easy
Description: You are given an m x n matrix M initialized with all 0's and an array of operations ops,
where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return the number of maximum integers in the matrix after performing all the operations."""

from typing import List


class Solution:
    @staticmethod
    def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
        """Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the minimum row and column
        min_row = m
        min_col = n
        # Iterate over each operation
        for op in ops:  # op: [2, 2], [3, 3]
            # Update the minimum row and column: only the minimum row and column matters
            min_row = min(min_row, op[0])  # min(3, 2) = 2
            min_col = min(min_col, op[1])  # min(3, 2) = 2
        return min_row * min_col


# Unit Test: Input: m = 3, n = 3, ops = [[2, 2], [3, 3]], Output: 4
assert Solution.maxCount(3, 3, [[2, 2], [3, 3]]) == 4

# Unit Test: Input: m = 3, n = 3, ops = [[2, 2], [3, 3], [3, 3]], Output: 4
assert Solution.maxCount(3, 3, [[2, 2], [3, 3], [3, 3]]) == 4

# Unit Test: Input: m = 3, n = 3, ops = [], Output: 9
assert Solution.maxCount(3, 3, []) == 9

print("All unit tests are passed")

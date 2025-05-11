"""598. Range Addition II
Link: https://leetcode.com/problems/range-addition-ii/
Difficulty: Easy
Description: You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return the number of maximum integers in the matrix after performing all the operations."""

from typing import List


class Solution:
    @staticmethod
    def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
        """Optimal Solution: Find Intersection. Time Complexity: O(n), Space Complexity: O(1)."""
        if not ops:
            return m * n
        # Find the intersection of all operations
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        return min(min_a, m) * min(min_b, n)


def unit_test():
    # Input: m = 3, n = 3, ops = [[2, 2], [3, 3]], Output: 4
    assert Solution.maxCount(3, 3, [[2, 2], [3, 3]]) == 4

    # Input: m = 3, n = 3, ops = [[2, 2], [3, 3], [3, 3]], Output: 4
    assert Solution.maxCount(3, 3, [[2, 2], [3, 3], [3, 3]]) == 4

    # Input: m = 3, n = 3, ops = [], Output: 9
    assert Solution.maxCount(3, 3, []) == 9


if __name__ == "__main__":
    unit_test()
    print("All unit tests are passed.")

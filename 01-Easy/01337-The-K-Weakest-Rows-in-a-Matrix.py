"""1337. The K Weakest Rows in a Matrix
Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
Difficulty: Easy
Description: You are given an m x n binary matrix mat of 1's (representing soldiers) and
0's (representing civilians). The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
- The number of soldiers in row i is less than the number of soldiers in row j.
- Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest."""

from typing import List


class Solution:
    @staticmethod
    def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
        """Optimal Solution: Tuple sorting.
           Time Complexity: O(m * n + m * log(m)), Space Complexity: O(m)"""
        # Count the number of soldiers in each row
        # E.g. [(2, 0), (3, 1), (1, 2), (2, 3), (5, 4)]
        soldiers = [(sum(row), i) for (i, row) in enumerate(mat)]

        # Sort the rows based on the number of soldiers: [(1, 2), (2, 0), (2, 3), (3, 1), (5, 4)]
        soldiers.sort()  # .sort() sorts the list in-place by the first element of each tuple

        # Return the indices of the k weakest rows: [:k] extracts the first k elements (not inclusive)
        return [i for (_, i) in soldiers[:k]]


# Unit Test: mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]],
# k = 3, Output: [2,0,3]
assert (Solution.kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0],
                               [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3)
        == [2, 0, 3])

# Unit Test: mat = [[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], k = 2, Output: [0,2]
assert (Solution.kWeakestRows([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2)
        == [0, 2])

print("All unit tests are passed.")

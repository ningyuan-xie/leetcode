"""2965. Find Missing and Repeated Values
Link: https://leetcode.com/problems/find-missing-and-repeated-values/
Difficulty: Easy
Description: You are given a 0-indexed 2D integer matrix grid of size n * n with values in the
range [1, n2]. Each integer appears exactly once except a which appears twice and b which is
missing. The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b."""

from typing import List


class Solution:
    @staticmethod
    def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
        """Optimal Solution: Counting Sort. Time Complexity: O(n^2), Space Complexity: O(n)"""
        n = len(grid)
        N = n * n  # Maximum value in the grid

        count = [0] * (N + 1)  # Frequency array for numbers from 1 to N

        # Count occurrences of each number in the grid
        for row in grid:
            for num in row:
                count[num] += 1

        repeated = missing = -1
        for i in range(1, N + 1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i
            if repeated != -1 and missing != -1:
                break  # Stop early if both found

        return [repeated, missing]


# Unit Test: grid = [[1,3],[2,2]], Output: [2,4]
assert Solution.findMissingAndRepeatedValues([[1, 3], [2, 2]]) == [2, 4]

# Unit Test: grid = [[9,1,7],[8,9,2],[3,4,6]], Output: [9,5]
assert Solution.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]) == [9, 5]

print("All unit tests are passed.")

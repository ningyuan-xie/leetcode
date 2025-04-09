"""2022. Convert 1D Array Into 2D Array
Link: https://leetcode.com/problems/convert-1d-array-into-2d-array/
Difficulty: Easy
Description: You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers,
m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using
all the elements from original.
The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the
constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second
row of the constructed 2D array, and so on.
Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it
is impossible."""

from typing import List


class Solution:
    @staticmethod
    def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
        """Optimal Solution: 2D Array. Time Complexity: O(m * n), Space Complexity: O(m * n)"""
        # Check if the length of the original array is equal to m * n
        if len(original) != m * n:
            return []

        # Initialize the 2D array
        result = []
        for i in range(0, len(original), n):  # range(start, stop, step), i = 0, n, 2n, 3n, ...
            result.append(original[i:i + n])

        return result


# Unit Test: original = [1, 2, 3, 4], m = 2, n = 2, Output: [[1, 2], [3, 4]]
assert Solution.construct2DArray([1, 2, 3, 4], 2, 2) == [[1, 2], [3, 4]]

# Unit Test: original = [1, 2, 3], m = 1, n = 3, Output: [[1, 2, 3]]
assert Solution.construct2DArray([1, 2, 3], 1, 3) == [[1, 2, 3]]

# Unit Test: original = [1, 2], m = 1, n = 1, Output: []
assert Solution.construct2DArray([1, 2], 1, 1) == []

print("All unit tests are passed")

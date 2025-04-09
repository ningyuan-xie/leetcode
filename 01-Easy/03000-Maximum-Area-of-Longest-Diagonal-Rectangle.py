"""3000. Maximum Area of Longest Diagonal Rectangle
Link: https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
Difficulty: Easy
Description: You are given a 2D 0-indexed integer array dimensions.
For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length
and dimensions[i][1] represents the width of the rectangle i.
Return the area of the rectangle having the longest diagonal. If there are multiple
rectangles with the longest diagonal, return the area of the rectangle having the
maximum area."""

from typing import List


class Solution:
    @staticmethod
    def areaOfMaxDiagonal(dimensions: List[List[int]]) -> int:
        """Optimal Solution: Math. Time Complexity: O(n), Space Complexity: O(1)"""
        max_area = 0
        longest_diagonal = 0

        def area(rectangle_input: List[int]) -> int:
            """Calculate the area of a rectangle"""
            return rectangle_input[0] * rectangle_input[1]

        def diagonal(rectangle_input: List[int]) -> int:
            """Calculate the diagonal of a rectangle"""
            return (rectangle_input[0] ** 2 + rectangle_input[1] ** 2) ** 0.5

        for rectangle in dimensions:
            if diagonal(rectangle) > longest_diagonal:
                longest_diagonal = diagonal(rectangle)
                max_area = area(rectangle)
            elif diagonal(rectangle) == longest_diagonal:
                max_area = max(max_area, area(rectangle))

        return max_area


# Unit Test: dimensions = [[9,3],[8,6]], Output = 48
assert Solution.areaOfMaxDiagonal([[9, 3], [8, 6]]) == 48

# Unit Test: dimensions = [[3,4],[4,3]], Output = 12
assert Solution.areaOfMaxDiagonal([[3, 4], [4, 3]]) == 12

print("All unit tests are passed")

"""3024. Type of Triangle
Link: https://leetcode.com/problems/type-of-triangle/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums of size 3 which can form the
sides of a triangle.
A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot
form a triangle."""

from typing import List


class Solution:
    @staticmethod
    def triangleType(nums: List[int]) -> str:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        a, b, c = sorted(nums)

        # Check if the triangle is valid
        if a + b <= c:
            return "none"

        # Check the type of triangle
        if a == b == c:
            return "equilateral"
        elif a == b or b == c:
            return "isosceles"
        else:
            return "scalene"


# Input: nums = [3,3,3], Output = "Equilateral"
assert Solution.triangleType([3, 3, 3]) == "Equilateral"

# Input: nums = [3,4,5], Output = "Scalene"
assert Solution.triangleType([3, 4, 5]) == "Scalene"

print("All unit tests are passed.")

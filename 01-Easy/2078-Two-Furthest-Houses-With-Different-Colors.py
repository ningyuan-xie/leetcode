"""2078. Two Furthest Houses With Different Colors
Link: https://leetcode.com/problems/Two-Furthest-Houses-With-Different-Colors
Difficulty: Easy
Description: There are n houses evenly lined up on the street, and each house is beautifully painted.
You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of
the ith house.
Return the maximum distance between two houses with different colors.
The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x."""

from typing import List


class Solution:
    @staticmethod
    def maxDistance(colors: List[int]) -> int:
        """Optimal Solution: Two Passes. Time Complexity: O(n), Space Complexity: O(1)"""
        n = len(colors)
        # Forward loop: Compare the first house to the farthest house with a different color
        max_dist1 = 0
        for i in range(n):
            if colors[i] != colors[0]:
                max_dist1 = max(max_dist1, i)

        # Forward loop: Compare the last house to the farthest house with a different color
        max_dist2 = 0
        for i in range(n):
            if colors[i] != colors[-1]:
                max_dist2 = max(max_dist2, n - 1 - i)

        return max(max_dist1, max_dist2)


# Unit Test: Input: colors = [1,1,1,6,1,1,1], Output: 3
assert Solution.maxDistance([1, 1, 1, 6, 1, 1, 1]) == 3

# Unit Test: Input: colors = [1,8,3,8,3], Output: 4
assert Solution.maxDistance([1, 8, 3, 8, 3]) == 4

# Unit Test: Input: colors = [0,1], Output: 1
assert Solution.maxDistance([0, 1]) == 1

# Unit Test: Input: colors = [4,4,4,11,4,4,11,4,4,4,4,4], Output: 8
assert Solution.maxDistance([4, 4, 4, 11, 4, 4, 11, 4, 4, 4, 4, 4]) == 8

print("All unit tests are passed")

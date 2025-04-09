"""1725. Number Of Rectangles That Can Form The Largest Square
Link: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
Difficulty: Easy
Description: You are given an array rectangles where rectangles[i] = [li, wi] represents the ith
rectangle of length li and width wi.
You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi.
For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at
most 4.
Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
Return the number of rectangles that can make a square with a side length of maxLen."""

from typing import List


class Solution:
    @staticmethod
    def count_good_rectangles(rectangles: List[List[int]]) -> int:
        """Optimal Solution: Counting. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the maximum side length & the number of rectangles that can form the largest square
        max_side = max_squares = 0

        # Count the number of rectangles that can form the largest square
        for (length, width) in rectangles:
            side = min(length, width)
            if side > max_side:
                max_side = side
                max_squares = 1  # Reset the count
            elif side == max_side:
                max_squares += 1

        return max_squares


# Unit Test: rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]], Output: 3
assert Solution.count_good_rectangles([[5, 8], [3, 9], [5, 12], [16, 5]]) == 3

# Unit Test: rectangles = [[2, 3], [3, 7], [4, 3], [3, 7]], Output: 3
assert Solution.count_good_rectangles([[2, 3], [3, 7], [4, 3], [3, 7]]) == 3

# Unit Test: rectangles = [[5, 8], [3, 9], [3, 12], [16, 5]], Output: 2
assert Solution.count_good_rectangles([[5, 8], [3, 9], [3, 12], [16, 5]]) == 2

print("All unit tests are passed.")

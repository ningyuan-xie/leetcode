"""836. Rectangle Overlap
Link: https://leetcode.com/problems/rectangle-overlap/
Difficulty: Easy
Description: An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is
the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner.
Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to
the Y-axis.
Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles
that only touch at the corner or edges do not overlap.
Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
"""

from typing import List


class Solution:
    @staticmethod
    def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
        """Optimal Solution: Check for Non-Overlap. Time Complexity: O(1), Space Complexity: O(1)"""
        # Check non-overlap: either one situation below is true, then no overlap
        return not (rec1[2] <= rec2[0] or  # rec1 is to the left of rec2
                    rec1[3] <= rec2[1] or  # rec1 is below rec2
                    rec1[0] >= rec2[2] or  # rec1 is to the right of rec2
                    rec1[1] >= rec2[3])  # rec1 is above rec2


# Unit Test: Input: rec1 = [0, 0, 2, 2], rec2 = [1, 1, 3, 3], Output: True
assert Solution.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]) is True

# Unit Test: Input: rec1 = [0, 0, 1, 1], rec2 = [1, 0, 2, 1], Output: False
assert Solution.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]) is False

# Unit Test: Input: rec1 = [0, 0, 1, 1], rec2 = [2, 2, 3, 3], Output: False
assert Solution.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]) is False

print("All unit tests are passed")

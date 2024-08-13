"""492. Construct the Rectangle
Link: https://leetcode.com/problems/construct-the-rectangle/
Difficulty: Easy
Description: A web developer needs to know how to design a web page's size.
So, given a specific rectangular web page’s area, your job by now is to design a
rectangular web page, whose length L and width W satisfy the following requirements:
1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you
designed in sequence."""

from typing import List


class Solution:
    @staticmethod
    def constructRectangle(area: int) -> List[int]:
        """Optimal Solution: Iteration. Time Complexity: O(sqrt(n)), Space Complexity: O(1).
           The trick is to use square root as an upper bound for the shorter side of the rectangle"""
        # Calculate the square root of the area as the upper bound for width
        width_upper_bound = int(area ** 0.5)  # E.g. area = 37 -> sqrt_area = 6
        # Iterate from the square root to 1
        for width in range(width_upper_bound, 0, -1):  # Stop at 1
            # If the area is divisible by the current number
            if area % width == 0:
                # Return the length and width immediately as W and L would be the closest
                return [area // width, width]


# Unit Test: Input: area = 4, Output: [2, 2]
assert Solution.constructRectangle(4) == [2, 2]

# Unit Test: Input: area = 37, Output: [37, 1]
assert Solution.constructRectangle(37) == [37, 1]

# Unit Test: Input: area = 122122, Output: [427, 286]
assert Solution.constructRectangle(122122) == [427, 286]

print("All unit tests are passed")

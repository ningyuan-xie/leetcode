"""492. Construct the Rectangle
Link: https://leetcode.com/problems/construct-the-rectangle/
Difficulty: Easy
Description: A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence."""

from typing import List


class Solution:
    @staticmethod
    def constructRectangle(area: int) -> List[int]:
        """Optimal Solution: Linear Search. Time Complexity: O(sqrt(n)), Space Complexity: O(1)."""
        # Initialize the width to the square root of the area
        width = int(area**0.5)

        # Iterate downwards to find the largest width that divides the area
        while area % width != 0:
            width -= 1

        # Calculate the length using the found width
        length = area // width

        return [length, width]



def unit_tests():
    # Input: area = 4, Output: [2, 2]
    assert Solution.constructRectangle(4) == [2, 2]

    # Input: area = 37, Output: [37, 1]
    assert Solution.constructRectangle(37) == [37, 1]

    # Input: area = 122122, Output: [427, 286]
    assert Solution.constructRectangle(122122) == [427, 286]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

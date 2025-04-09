"""661. Image Smoother
Link: https://leetcode.com/problems/image-smoother/
Difficulty: Easy
Description: An image smoother is a filter of the size 3 x 3 that can be applied to each cell of
an image by rounding down the average of the cell and the eight surrounding cells (i.e., the
average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell
is not present, we do not consider it in the average. Given an m x n integer matrix img representing
the grayscale of an image, return the image after applying the smoother on each cell of it."""

from typing import List


class Solution:
    @staticmethod
    def imageSmoother(img: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: 2D Convolution. Time Complexity: O(m * n), Space Complexity: O(m * n)"""
        # Get the dimensions of the image
        row, column = len(img), len(img[0])  # 3, 3

        # Initialize the smoothed image
        smoothed_img = [[0] * column for _ in range(row)]

        # Define the 8 directions for the 3 x 3 smoother
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 0), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for r in range(row):  # 0, 1, 2
            for c in range(column):  # 0, 1, 2
                # Initialize the sum and the count of the surrounding cells
                total, count = 0, 0

                # Traverse the 3 x 3 smoother and find the sum and the count of the surrounding cells
                for (dr, dc) in directions:
                    # Check if the neighbor cell (nr, nc) is within the image
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < column:
                        total += img[nr][nc]
                        count += 1

                # Update the smoothed image
                smoothed_img[r][c] = total // count
        return smoothed_img


# Unit Test: Input: img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]], Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert Solution.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Unit Test: Input: img = [[100,200,100],[200,50,200],[100,200,100]],
# Output: [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
assert (Solution.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) ==
        [[137, 141, 137], [141, 138, 141], [137, 141, 137]])

print("All unit tests are passed")

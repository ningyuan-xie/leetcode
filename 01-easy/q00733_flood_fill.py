"""733. Flood Fill
Link: https://leetcode.com/problems/flood-fill/
Difficulty: Easy
Description: You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill:
1. Begin with the starting pixel and change its color to color.
2. Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
3. Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
4. The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill."""

from typing import List


class Solution:
    @staticmethod
    def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """Optimal Solution: Preorder DFS. Time Complexity: O(m*n), Space Complexity: O(m*n)."""
        # Get the original color of the starting pixel
        original_color = image[sr][sc]

        # Check if the original color is the same as the new color
        if original_color == color:
            return image

        # Directions for 4-way movement
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        def preorder(r: int, c: int) -> None:
            """Helper function to perform preorder DFS."""
            # Update the current pixel's color
            image[r][c] = color
            
            # Check all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check if new coordinates are valid and color matches original
                if (0 <= nr < len(image) and 0 <= nc < len(image[0]) 
                    and image[nr][nc] == original_color):
                    preorder(nr, nc)

        preorder(sr, sc)
        return image


def unit_tests():
    # Input: image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, newColor = 2, Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert Solution.flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    # Input: image = [[0, 0, 0], [0, 1, 1]], sr = 1, sc = 1, newColor = 1, Output: [[0, 0, 0], [0, 1, 1]]
    assert Solution.flood_fill([[0, 0, 0], [0, 1, 1]], 1, 1, 1) == [[0, 0, 0], [0, 1, 1]]

    # Input: image = [[0, 0, 0], [0, 1, 1]], sr = 1, sc = 1, newColor = 2, Output: [[0, 0, 0], [0, 2, 2]]
    assert Solution.flood_fill([[0, 0, 0], [0, 1, 1]], 1, 1, 2) == [[0, 0, 0], [0, 2, 2]]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

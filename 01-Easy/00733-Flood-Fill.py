"""733. Flood Fill
Link: https://leetcode.com/problems/flood-fill/
Difficulty: Easy
Description: An image is represented by an m x n integer grid image where image[i][j] represents
the pixel value of the image. You are also given three integers sr, sc, and newColor.
You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally
to the starting pixel of the same color as the starting pixel, plus any pixels connected
4-directionally to those pixels (also with the same color), and so on. Replace the color of all
of the aforementioned pixels with color.
Return the modified image after performing the flood fill."""

from typing import List


class Solution:
    @staticmethod
    def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """Optimal Solution: Preorder DFS Traversal.
           Time Complexity: O(m * n), Space Complexity: O(m * n)"""
        # Get the original color of the starting pixel
        original_color = image[sr][sc]

        # Check if the original color is the same as the new color
        if original_color == color:
            # If so, do nothing and return the original image
            return image

        # Perform depth-first search
        Solution.preorder_dfs_traversal(image, sr, sc, original_color, color)

        # Return the updated image
        return image

    @staticmethod
    def preorder_dfs_traversal(image: List[List[int]], r: int, c: int,
                               original_color: int, new_color: int) -> None:
        """Helper function to perform depth-first search"""
        # Check if the current pixel is out of bounds or has a different color
        if (r < 0 or r >= len(image)
                or c < 0 or c >= len(image[0])
                # color is initially not the original color or already changed
                or image[r][c] != original_color):
            # If so, return
            return

        # Update the color of the current pixel
        image[r][c] = new_color

        # Recursively call dfs on the neighboring pixels
        Solution.preorder_dfs_traversal(image, r - 1, c, original_color, new_color)  # Up
        Solution.preorder_dfs_traversal(image, r + 1, c, original_color, new_color)  # Down
        Solution.preorder_dfs_traversal(image, r, c - 1, original_color, new_color)  # Left
        Solution.preorder_dfs_traversal(image, r, c + 1, original_color, new_color)  # Right


# Input: image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, newColor = 2,
# Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
assert (Solution.flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
        == [[2, 2, 2], [2, 2, 0], [2, 0, 1]])

# Input: image = [[0, 0, 0], [0, 1, 1]], sr = 1, sc = 1, newColor = 1,
# Output: [[0, 0, 0], [0, 1, 1]]
assert (Solution.flood_fill([[0, 0, 0], [0, 1, 1]], 1, 1, 1)
        == [[0, 0, 0], [0, 1, 1]])

# Input: image = [[0, 0, 0], [0, 1, 1]], sr = 1, sc = 1, newColor = 2,
# Output: [[0, 0, 0], [0, 2, 2]]
assert (Solution.flood_fill([[0, 0, 0], [0, 1, 1]], 1, 1, 2)
        == [[0, 0, 0], [0, 2, 2]])

print("All unit tests are passed.")

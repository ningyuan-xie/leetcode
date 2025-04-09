"""832. Flipping an Image
Link: https://leetcode.com/problems/flipping-an-image/
Difficulty: Easy
Description: Given an n x n binary matrix image, flip the image horizontally, then invert it,
and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0]."""

from typing import List


class Solution:
    @staticmethod
    def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Get the length of the image
        n = len(image)
        # Iterate through each row
        for row in image:  # E.g. [1, 1, 0], [1, 0, 1], [0, 0, 0]
            # Initialize the pointers
            left, right = 0, n - 1
            # Flip the row horizontally first
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1

            # Next, invert the row
            row[:] = [1 - pixel for pixel in row]

        return image


# Input: image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]],
# Output: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
assert (Solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) ==
        [[1, 0, 0], [0, 1, 0], [1, 1, 1]])

# Input: image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
# Output: [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
assert (Solution.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) ==
        [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]])

print("All unit tests are passed.")

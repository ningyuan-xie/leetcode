"""832. Flipping an Image
Link: https://leetcode.com/problems/flipping-an-image/
Difficulty: Easy
Description: Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
• For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
• For example, inverting [0,1,1] results in [1,0,0]."""

from typing import List


class Solution:
    @staticmethod
    def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                # Flip and invert in one operation
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
        return image


def unit_tests():
    # Input: image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]], Output: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert Solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    # Input: image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]], Output: [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    assert Solution.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) == [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]


if __name__ == '__main__':
    unit_tests()
    print("All unit tests are passed.")

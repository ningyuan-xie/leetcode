"""661. Image Smoother
Link: https://leetcode.com/problems/image-smoother/
Difficulty: Easy
Description: An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother)."""

from typing import List


class Solution:
    @staticmethod
    def imageSmoother(img: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: 2D Convolution. Time Complexity: O(m*n), Space Complexity: O(m*n)."""
        m, n = len(img), len(img[0])
        result = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total = count = 0
                # Check all 8 surrounding cells plus current cell
                for x in (i-1, i, i+1):
                    for y in (j-1, j, j+1):
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1
                result[i][j] = total // count
        return result


def unit_tests():
    # Input: img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]], Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert Solution.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Input: img = [[100,200,100],[200,50,200],[100,200,100]], Output: [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
    assert Solution.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [[137, 141, 137], [141, 138, 141], [137, 141, 137]]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

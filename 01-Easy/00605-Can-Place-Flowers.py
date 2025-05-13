"""605. Can Place Flowers
Link: https://leetcode.com/problems/can-place-flowers/
Difficulty: Easy
Description: You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        """Optimal Solution: Greedy. Time Complexity: O(n), Space Complexity: O(1)."""
        count = 0

        # Iterate over the flowerbed
        for i in range(len(flowerbed)):
            # If the current plot is empty
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or out of bounds
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    # Stop early if we have planted enough flowers
                    if count >= n:
                        return True
        return count >= n


def unit_test():
    # Input: flowerbed = [1,0,0,0,1], n = 1, Output: True
    assert Solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True

    # Input: flowerbed = [1,0,0,0,1], n = 2, Output: False
    assert Solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False

    # Input: flowerbed = [0,0,1,0,0], n = 1, Output: True
    assert Solution.canPlaceFlowers([0, 0, 1, 0, 0], 1) is True

    # Input: flowerbed = [0,0,1,0,0], n = 2, Output: True
    assert Solution.canPlaceFlowers([0, 0, 1, 0, 0], 2) is True


if __name__ == "__main__":
    unit_test()
    print("All unit tests are passed.")

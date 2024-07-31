# Link: https://leetcode.com/problems/can-place-flowers/
# Difficulty: Easy
# Description: You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not
# empty, and an integer n, return true if n new flowers can be planted in the flowerbed without
# violating the no-adjacent-flowers rule and false otherwise.

from typing import List


class Solution:
    # Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        # Initialize the number of flowers that can be planted
        flowers_planted = 0
        # Initialize the length of the flowerbed
        length = len(flowerbed)
        # Initialize the index of the flowerbed
        index = 0
        # Iterate over the flowerbed
        while index < length:
            # If the current plot is empty
            if flowerbed[index] == 0:
                # Check if the previous and next plots are empty
                prev_plot = flowerbed[index - 1] if index > 0 else 0
                next_plot = flowerbed[index + 1] if index < length - 1 else 0
                # If the previous and next plots are empty
                if prev_plot == 0 and next_plot == 0:
                    # Plant a flower
                    flowerbed[index] = 1
                    # Increment the number of flowers planted
                    flowers_planted += 1
            # Move to the next plot
            index += 1
        return flowers_planted >= n


# Unit Test: Input: flowerbed = [1,0,0,0,1], n = 1, Output: True
assert Solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True

# Unit Test: Input: flowerbed = [1,0,0,0,1], n = 2, Output: False
assert Solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False

# Unit Test: Input: flowerbed = [0,0,1,0,0], n = 1, Output: True
assert Solution.canPlaceFlowers([0, 0, 1, 0, 0], 1) is True

# Unit Test: Input: flowerbed = [0,0,1,0,0], n = 2, Output: True
assert Solution.canPlaceFlowers([0, 0, 1, 0, 0], 2) is True

print("All unit tests are passed")

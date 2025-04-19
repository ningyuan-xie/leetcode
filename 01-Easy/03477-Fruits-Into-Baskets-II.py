"""3477. Fruits Into Baskets II
Link: https://leetcode.com/problems/fruits-into-baskets-ii/
Difficulty: Easy
Description: You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
From left to right, place the fruits according to these rules:
• Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
• Each basket can hold only one type of fruit.
• If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made."""

from typing import List


class Solution:
    @staticmethod
    def maxFruits(fruits: List[int], baskets: List[int]) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(n^2), Space Complexity: O(1)."""
        n = len(fruits)
        unplaced = 0

        # Check every fruit with every basket
        for i in range(n):
            placed = False
            for j in range(n):
                # If the fruit can be placed in the basket
                if fruits[i] <= baskets[j]:
                    # Place the fruit in the basket
                    baskets[j] = 0
                    placed = True
                    break

            # If the fruit could not be placed in any basket, increment unplaced count
            if not placed:
                unplaced += 1
        
        # Return the number of unplaced fruits
        return unplaced


def unit_tests():
    # Input: fruits = [4,2,5], baskets = [3,5,4], Output: 1
    # assert Solution.maxFruits([4, 2, 5], [3, 5, 4]) == 1

    # Input: fruits = [3,6,1], baskets = [6,4,7], Output: 0
    assert Solution.maxFruits([3, 6, 1], [6, 4, 7]) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

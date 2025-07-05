"""1217. Minimum Cost to Move Chips to The Same Position
Link: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
Difficulty: Easy
Description: We have n chips, where the position of the ith chip is position[i].
We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:
• position[i] + 2 or position[i] - 2 with cost = 0.
• position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position."""

from typing import List


class Solution:
    @staticmethod
    def minCostToMoveChips(position: List[int]) -> int:
        """Optimal Solution: Counting Odd and Even Positions. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the number of chips at odd and even positions
        odd_count, even_count = 0, 0

        # Count the number of chips at odd and even positions
        for pos in position:  # E.g. [2, 2, 2, 3, 3]
            if pos % 2 == 0:
                even_count += 1  # number of chips at even positions = 3
            else:
                odd_count += 1  # number of chips at odd positions = 2

        # Regardless of actual positions, all the odd/even positions can be viewed as the same position, so pick the smaller number of chips between odd and even positions to move
        return min(odd_count, even_count)


def unit_tests():
    # Input: position = [1, 2, 3], Output: 1
    assert Solution.minCostToMoveChips([1, 2, 3]) == 1

    # Input: position = [2, 2, 2, 3, 3], Output: 2
    assert Solution.minCostToMoveChips([2, 2, 2, 3, 3]) == 2

    # Input: position = [1, 1000000000], Output: 1
    assert Solution.minCostToMoveChips([1, 1000000000]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

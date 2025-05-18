"""2335. Minimum Amount of Time to Fill Cups
Link: https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
Difficulty: Easy
Description: You have a water dispenser that can dispense cold, warm, and hot water. Every second, you
can either fill up 2 cups with different types of water, or 1 cup of any type of water.
You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2]
denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum
number of seconds needed to fill up all the cups."""

from typing import List


class Solution:
    @staticmethod
    def fillCups(amount: List[int]) -> int:
        """Optimal Solution: Greedy Approach. Time Complexity: O(1), Space Complexity: O(1)."""
        # Sort the array to always work with the largest two values
        amount.sort()  # [1, 4, 2] -> [1, 2, 4]

        # If the largest amount is greater than the sum of the other two, we can fill cups using the
        # largest and one of the smaller cups: the time needed would be equal to the largest value
        if amount[2] > amount[0] + amount[1]:
            return amount[2]
        else:
            # Otherwise, the time needed is at least half the total sum (rounded up)
            return (sum(amount) + 1) // 2


# Unit Test: amount = [1,4,2], Output: 4
assert Solution.fillCups([1, 4, 2]) == 4

# Unit Test: amount = [5,4,4], Output: 7
assert Solution.fillCups([5, 4, 4]) == 7

print("All unit tests are passed.")

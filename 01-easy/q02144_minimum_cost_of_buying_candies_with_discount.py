"""2144. Minimum Cost of Buying Candies With Discount
Link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
Difficulty: Easy
Description: A shop is selling candies at a discount. For every two candies sold, the shop gives a
third candy for free.
The customer can choose any candy to take away for free as long as the cost of the chosen candy is
less than or equal to the minimum cost of the two candies bought.
- For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with
costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the
minimum cost of buying all the candies."""

from typing import List


class Solution:
    @staticmethod
    def minimumCost(cost: List[int]) -> int:
        """Optimal Solution: Sorting. Time Complexity: O(nlogn), Space Complexity: O(1)."""
        cost.sort(reverse=True)  # [6,5,7,9,2,2] -> [9,7,6,5,2,2]
        n = len(cost)
        total = 0

        for i in range(n):
            # Every two candies, the third candy is free
            if i % 3 == 2:
                continue
            total += cost[i]
        return total


# Input: cost = [1,2,3], Output: 5
assert Solution.minimumCost([1, 2, 3]) == 5

# Input: cost = [6,5,7,9,2,2], Output: 23
assert Solution.minimumCost([6, 5, 7, 9, 2, 2]) == 23

# Input: cost = [5,5], Output: 10
assert Solution.minimumCost([5, 5]) == 10

print("All unit tests are passed.")

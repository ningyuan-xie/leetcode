"""2706. Buy Two Chocolates
Link: https://leetcode.com/problems/buy-two-chocolates/
Difficulty: Easy
Description: You are given an integer array prices representing the prices of various chocolates in a
store. You are also given a single integer money, which represents your initial amount of money.
You must buy exactly two chocolates in such a way that you still have some non-negative leftover money.
You would like to minimize the sum of the prices of the two chocolates you buy.
Return the amount of money you will have leftover after buying the two chocolates. If there is no way
for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be
non-negative."""

from typing import List


class Solution:
    @staticmethod
    def buyChoco(prices: List[int], money: int) -> int:
        """Optimal Solution: Sort. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        # Sort the prices
        prices.sort()
        money -= prices[0] + prices[1]
        return money if money >= 0 else money + prices[0] + prices[1]


# Unit Test: prices = [1,2,2], money = 3, Output: 0
assert Solution.buyChoco([1, 2, 2], 3) == 0

# Unit Test: prices = [3,2,3], money = 3, Output: 3
assert Solution.buyChoco([3, 2, 3], 3) == 3

print("All unit tests are passed.")

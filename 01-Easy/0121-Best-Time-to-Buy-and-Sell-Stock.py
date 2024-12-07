"""121. Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Description: You are given an array prices where prices[i] is
the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock."""

from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 2016-Maximum-Difference-Between-Increasing-Elements.py"""
        # Initialize the maximum profit
        max_profit = 0
        # Initialize the minimum price encountered so far
        min_price = prices[0]

        for i in range(1, len(prices)):
            # Update the maximum profit
            max_profit = max(max_profit, prices[i] - min_price)
            # Update the minimum price encountered so far
            min_price = min(min_price, prices[i])

        return max_profit


# Unit Test: Input: prices = [7,1,5,3,6,4], Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5
assert Solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5

# Unit Test: Input: prices = [7,6,4,3,1], Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0
assert Solution.maxProfit([7, 6, 4, 3, 1]) == 0

# Unit Test: Input: prices = [1,2], Output: 1
# Explanation: Buy on day 1 (price = 1) and sell on day 2 (price = 2), profit = 2-1 = 1
assert Solution.maxProfit([1, 2]) == 1

# Unit Test: Input: prices = [2,4,1], Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2
assert Solution.maxProfit([2, 4, 1]) == 2

# Unit Test: Input: prices = [2,1,2,0,1], Output: 1
# Explanation: Buy on day 2 (price = 1) and sell on day 4 (price = 2), profit = 2-1 = 1
assert Solution.maxProfit([2, 1, 2, 0, 1]) == 1

print("All unit tests are passed")

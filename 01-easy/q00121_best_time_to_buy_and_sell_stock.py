"""121. Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Description: You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the minimum price and maximum profit
        min_price = float('inf')
        max_profit = 0

        # Iterate through the prices
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit if selling at the current price
            profit = price - min_price
            # Update the maximum profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit


def unit_tests():
    # Input: prices = [7,1,5,3,6,4], Output: 5
    assert Solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    # Input: prices = [7,6,4,3,1], Output: 0
    assert Solution.maxProfit([7, 6, 4, 3, 1]) == 0

    # Input: prices = [1,2], Output: 1
    assert Solution.maxProfit([1, 2]) == 1

    # Input: prices = [2,4,1], Output: 2
    assert Solution.maxProfit([2, 4, 1]) == 2

    # Input: prices = [2,1,2,0,1], Output: 1
    assert Solution.maxProfit([2, 1, 2, 0, 1]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

"""1475. Final Prices With a Special Discount in a Shop
Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
Difficulty: Easy
Description: You are given an integer array prices where prices[i] is the price of the ith item in
a shop.
There is a special discount for items in the shop. If you buy the ith item, then you will receive
a discount equivalent to prices[j] where j is the minimum index such that j > i and
prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
Return an integer array answer where answer[i] is the final price you will pay for the ith item
of the shop, considering the special discount."""

from typing import List


class Solution:
    @staticmethod
    def finalPrices(prices: List[int]) -> List[int]:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(n)"""
        # Initialize the final prices array
        final_prices = []

        # Iterate through the prices array
        for i in range(len(prices)):
            # Initialize the discount
            discount = 0

            # Iterate through the prices array starting from the (i+1)th element
            for j in range(i + 1, len(prices)):
                # If the jth element is less than or equal to the ith element
                if prices[j] <= prices[i]:
                    # Set the discount to the jth element
                    discount = prices[j]
                    # Break out of the loop
                    break

            # Append the final price to the final prices array
            final_prices.append(prices[i] - discount)

        # Return the final prices array
        return final_prices


# Unit Test: prices = [8, 4, 6, 2, 3], Output: [4, 2, 4, 2, 3]
assert Solution.finalPrices([8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]

# Unit Test: prices = [1, 2, 3, 4, 5], Output: [1, 2, 3, 4, 5]
assert Solution.finalPrices([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Unit Test: prices = [10, 1, 1, 6], Output: [9, 0, 1, 6]
assert Solution.finalPrices([10, 1, 1, 6]) == [9, 0, 1, 6]

# Unit Test: prices = [10, 1, 1, 6, 3], Output: [9, 0, 1, 3, 3]
assert Solution.finalPrices([10, 1, 1, 6, 3]) == [9, 0, 1, 3, 3]

print("All unit tests are passed.")

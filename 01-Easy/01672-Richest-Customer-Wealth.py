"""1672. Richest Customer Wealth
Link: https://leetcode.com/problems/richest-customer-wealth/
Difficulty: Easy
Description: You are given an m x n integer grid accounts where accounts[i][j] is the amount of
money the ithcustomer has in the jth bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer
is the customer that has the maximum wealth."""

from typing import List


class Solution:
    @staticmethod
    def maximumWealth(accounts: List[List[int]]) -> int:
        """Optimal Solution: 2D Array. Time Complexity: O(m * n), Space Complexity: O(1)"""
        # Initialize the maximum wealth to 0
        max_wealth = 0

        # Traverse the 2D array and calculate the wealth of each customer
        for account in accounts:
            # Calculate the wealth of the customer
            wealth = sum(account)

            # Update the maximum wealth if the current customer's wealth is greater
            max_wealth = max(max_wealth, wealth)

        return max_wealth


# Unit Test: accounts = [[1, 2, 3], [3, 2, 1]], Output: 6
assert Solution.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6

# Unit Test: accounts = [[1, 5], [7, 3], [3, 5]], Output: 10
assert Solution.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10

# Unit Test: accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]], Output: 17
assert Solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17

print("All unit tests are passed.")

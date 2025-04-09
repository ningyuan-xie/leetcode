"""1716. Calculate Money in Leetcode Bank
Link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
Difficulty: Easy
Description: Hercy wants to save money for his first car. He puts money in the Leetcode bank
every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will
put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the
previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the
nth day."""


class Solution:
    @staticmethod
    def total_money(n: int) -> int:
        """Optimal Solution: Arithmetic Progression. Time Complexity: O(n), Space Complexity: O(1)"""
        # Calculate the number of full weeks and days
        weeks, days = n // 7, n % 7  # n = 4 -> weeks = 0, days = 4; n = 7 -> weeks = 1, days = 0

        # Calculate the total money for full weeks:
        # Base weeks: 1 + 2 + ... + 7 = 28
        # All subsequent weeks additions: [1 + (weeks - 1)] * (weeks - 1) // 2 * 7
        total_money = (28 * weeks + 7 * (weeks - 1) * weeks // 2)

        # Calculate the total money for the remaining days
        # All subsequent days: [(weeks + 1) + (weeks + days)] * days // 2
        total_money += (weeks + 1 + weeks + days) * days // 2

        return total_money


# Unit Test: n = 4, Output: 10
assert Solution.total_money(4) == 10

# Unit Test: n = 10, Output: 37
assert Solution.total_money(10) == 37

# Unit Test: n = 20, Output: 96
assert Solution.total_money(20) == 96

print("All unit tests are passed")

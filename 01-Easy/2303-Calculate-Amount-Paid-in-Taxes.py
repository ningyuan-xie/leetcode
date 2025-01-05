"""2303. Calculate Amount Paid in Taxes
Link: https://www.leetcode.com/problems/calculate-amount-paid-in-taxes/
Difficulty: Easy
Description: You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti]
means that the ith tax bracket has an upper bound of upperi and is taxed at a rate of percenti.
The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).
Tax is calculated as follows:
- The first upper0 dollars earned are taxed at a rate of percent0.
- The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
- The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
- And so on.
You are given an integer income representing the amount of money you earned. Return the amount of money
that you have to pay in taxes. Answers within 10-5 of the actual answer will be accepted."""

from typing import List


class Solution:
    @staticmethod
    def calculateTax(brackets: List[List[int]], income: int) -> float:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(1)"""
        tax_paid = 0.0
        previous_limit = 0  # Start from the lower limit of the first bracket

        for (upper_limit, rate) in brackets:
            if income <= previous_limit:
                break  # No more taxable income in the remaining brackets

            # Taxable income within the current bracket
            taxable_income = min(income, upper_limit) - previous_limit
            tax_paid += taxable_income * rate / 100  # Apply the tax rate
            previous_limit = upper_limit  # Update the lower limit for the next bracket

        return tax_paid


# Unit Test: brackets = [[3,50],[7,10],[12,25]], income = 10, Output: 2.65
assert Solution.calculateTax([[3, 50], [7, 10], [12, 25]], 10) == 2.65

# Unit Test: brackets = [[1,0],[4,25],[5,50]], income = 2, Output: 0.25
assert Solution.calculateTax([[1, 0], [4, 25], [5, 50]], 2) == 0.25

# Unit Test: brackets = [[2,50]], income = 0, Output: 0
assert Solution.calculateTax([[2, 50]], 0) == 0

print("All unit tests are passed")

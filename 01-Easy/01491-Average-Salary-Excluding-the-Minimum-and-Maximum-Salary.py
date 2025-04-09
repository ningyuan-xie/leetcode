"""1491. Average Salary Excluding the Minimum and Maximum Salary
Link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
Difficulty: Easy
Description: You are given an array of unique integers salary where salary[i] is the salary of
the ith employee.
Return the average salary of employees excluding the minimum and maximum salary.
Answers within 10-5 of the actual answer will be accepted."""

from typing import List


class Solution:
    @staticmethod
    def average(salary: List[int]) -> float:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the minimum and maximum salary
        min_salary, max_salary = float("inf"), float("-inf")
        # Initialize the sum
        total = 0

        # Iterate through the salary array
        for s in salary:
            # Update the minimum and maximum salary
            min_salary = min(min_salary, s)
            max_salary = max(max_salary, s)
            # Update the sum
            total += s

        # Return the average salary excluding the minimum and maximum salary
        return (total - min_salary - max_salary) / (len(salary) - 2)


# Unit Test: salary = [4000, 3000, 1000, 2000], Output: 2500.00000
assert Solution.average([4000, 3000, 1000, 2000]) == 2500.00000

# Unit Test: salary = [1000, 2000, 3000], Output: 2000.00000
assert Solution.average([1000, 2000, 3000]) == 2000.000

# Unit Test: salary = [6000, 5000, 4000, 3000, 2000, 1000], Output: 3500.00000
assert Solution.average([6000, 5000, 4000, 3000, 2000, 1000]) == 3500.00000

print("All unit tests are passed.")

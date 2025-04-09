"""2798. Number of Employees Who Met the Target
Link: https://leetcode.com/problems/number-of-employees-who-met-the-target/
Difficulty: Easy
Description: There are n employees in a company, numbered from 0 to n - 1. Each employee i has
worked for hours[i] hours in the company.
The company requires each employee to work for at least target hours.
You are given a 0-indexed array of non-negative integers hours of length n and a non-negative
integer target.
Return the integer denoting the number of employees who worked at least target hours."""

from typing import List


class Solution:
    @staticmethod
    def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        count = 0
        for hour in hours:
            if hour >= target:
                count += 1

        return count


# Unit Test: hours = [0,1,2,3,4], target = 2, Output: 3
assert Solution.numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2) == 3

# Unit Test: hours = [5,1,4,2,2], target = 6, Output: 0
assert Solution.numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6) == 0

print("All unit tests are passed.")

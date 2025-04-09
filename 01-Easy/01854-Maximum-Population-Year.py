"""1854. Maximum Population Year
Link: https://leetcode.com/problems/maximum-population-year/
Difficulty: Easy
Description: You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates
the birth and death years of the ith person.
The population of some year x is the number of people alive during that year. The ith person is
counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that
the person is not counted in the year that they die.
Return the earliest year with the maximum population."""

from typing import List


class Solution:
    @staticmethod
    def maximumPopulation(logs: List[List[int]]) -> int:
        """Optimal Solution: Range Count. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the population count: [0, 0, 0, ..., 0]
        population = [0] * 101

        # Iterate through the logs
        for log in logs:
            # Increment the population count for each year: [0, 0, 0, ..., 1, 1, 1, ..., 0]
            for year in range(log[0], log[1]):  # log[1] is exclusive
                population[year - 1950] += 1  # 1950 is the base year

        # Find the maximum population year
        max_population = max(population)

        # Return the maximum population year that is the earliest
        return population.index(max_population) + 1950


# Unit Test: logs = [[1993, 1999], [2000, 2010]], Output: 1993
assert Solution.maximumPopulation([[1993, 1999], [2000, 2010]]) == 1993

# Unit Test: logs = [[1950, 1961], [1960, 1971], [1970, 1981]], Output: 1960
assert Solution.maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]) == 1960

print("All unit tests are passed")

"""2427. Number of Common Factors
Link: https://leetcode.com/problems/number-of-common-factors/
Difficulty: Easy
Description: Given two positive integers a and b, return the number of common factors of a and b.
An integer x is a common factor of a and b if x divides both a and b."""


class Solution:
    @staticmethod
    def commonFactors(a: int, b: int) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(min(a, b)), Space Complexity: O(1)"""
        # Count the number of common factors
        common_factors = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                common_factors += 1
        return common_factors


# Unit Test: a = 12, b = 6, Output: 4
assert Solution.commonFactors(12, 6) == 4

# Unit Test: a = 25, b = 30, Output: 2
assert Solution.commonFactors(25, 30) == 2

print("All unit tests are passed.")

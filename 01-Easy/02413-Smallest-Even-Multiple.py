"""2413. Smallest Even Multiple
Link: https://leetcode.com/problems/smallest-even-multiple/
Difficulty: Easy
Description: Given a positive integer n, return the smallest positive integer that is a multiple of
both 2 and n."""


class Solution:
    @staticmethod
    def smallestEvenMultiple(n: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)"""
        return n if n % 2 == 0 else n * 2


# Unit Test: n = 5, Output: 10
assert Solution.smallestEvenMultiple(5) == 10

# Unit Test: n = 6, Output: 6
assert Solution.smallestEvenMultiple(6) == 6

print("All unit tests are passed.")

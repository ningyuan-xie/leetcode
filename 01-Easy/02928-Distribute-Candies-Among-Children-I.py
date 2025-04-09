"""2928. Distribute Candies Among Children I
Link: https://leetcode.com/problems/distribute-candies-among-children-i/
Difficulty: Easy
Description: You are given two positive integers n and limit.
Return the total number of ways to distribute n candies among 3 children such that no child gets
more than limit candies."""


class Solution:
    @staticmethod
    def distributeCandies(n: int, limit: int) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^3), Space Complexity: O(1)."""
        count = 0

        # Iterate through all possible ways to distribute candies among 3 children
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        count += 1

        return count


# Unit Test: n = 5, limit = 2, Output: 3
assert Solution.distributeCandies(5, 2) == 3

# Unit Test: n = 3, limit = 3, Output: 10
assert Solution.distributeCandies(3, 3) == 10

print("All unit tests are passed.")

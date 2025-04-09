"""1431. Kids With the Greatest Number of Candies
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Difficulty: Easy
Description: There are n kids with candies. You are given an integer array candies, where each
candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting
the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all
the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies."""

from typing import List


class Solution:
    @staticmethod
    def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(n)"""
        # Find the current max number of candies
        max_candies = max(candies)

        # Check if the kid can have the greatest number of candies
        return [(candies[i] + extraCandies) >= max_candies for i in range(len(candies))]


# Unit Test: candies = [2, 3, 5, 1, 3], extraCandies = 3, Output: [True, True, True, False, True]
assert (Solution.kidsWithCandies([2, 3, 5, 1, 3], 3)
        == [True, True, True, False, True])

# Unit Test: candies = [4, 2, 1, 1, 2], extraCandies = 1, Output: [True, False, False, False, False]
assert (Solution.kidsWithCandies([4, 2, 1, 1, 2], 1)
        == [True, False, False, False, False])

# Unit Test: candies = [12, 1, 12], extraCandies = 10, Output: [True, False, True]
assert Solution.kidsWithCandies([12, 1, 12], 10) == [True, False, True]

print("All unit tests are passed.")

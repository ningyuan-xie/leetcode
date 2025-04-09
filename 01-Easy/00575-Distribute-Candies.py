"""575. Distribute Candies
Link: https://leetcode.com/problems/distribute-candies/
Difficulty: Easy
Description: Alice has n candies, where the ith candy is of type candyType[i].
Alice noticed that she started to gain weight, so she visited a doctor.
The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
Alice likes her candies very much, and she wants to eat the maximum number of different types of
candies while still following the doctor's advice.
Given the integer array candyType of length n, return the maximum number of different types of
candies she can eat if she only eats n / 2 of them."""

from typing import List


class Solution:
    @staticmethod
    def distributeCandies(candyType: List[int]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n).
           The trick is to use a set to store the unique candies and compare its length with n / 2"""
        # Get the number of candies Alice can eat
        n = len(candyType)
        n_eat = n // 2
        # Get the number of unique types of candies
        unique_candies = set(candyType)
        n_unique = len(unique_candies)
        # Return the maximum number of different types of candies Alice can eat
        return min(n_eat, n_unique)


# Input: candyType = [1, 1, 2, 2, 3, 3], Output: 3
assert Solution.distributeCandies([1, 1, 2, 2, 3, 3]) == 3

# Input: candyType = [1, 1, 2, 3], Output: 2
assert Solution.distributeCandies([1, 1, 2, 3]) == 2

# Input: candyType = [6, 6, 6, 6], Output: 1
assert Solution.distributeCandies([6, 6, 6, 6]) == 1

# Input: candyType = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3], Output: 3
assert Solution.distributeCandies([1, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3

print("All unit tests are passed.")

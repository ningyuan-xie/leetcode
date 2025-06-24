"""1523. Count Odd Numbers in an Interval Range
Link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
Difficulty: Easy
Description: Given two non-negative integers low and high. Return the count of odd numbers between
low and high (inclusive)."""


class Solution:
    @staticmethod
    def countOdds(low: int, high: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        # Calculate the number of odd numbers between 0 and high
        count_high = (high + 1) // 2  # E.g. high = 7 -> count_high = 4; high = 10 -> count_high = 5
        # Calculate the number of odd numbers between 0 and low - 1
        count_low = low // 2  # E.g. low = 3 -> count_low = 1; low = 8 -> count_low = 4
        # Return the difference between the two counts
        return count_high - count_low


# Input: low = 3, high = 7, Output: 3
assert Solution.countOdds(3, 7) == 3

# Input: low = 8, high = 10, Output: 1
assert Solution.countOdds(8, 10) == 1

# Input: low = 1, high = 1, Output: 1
assert Solution.countOdds(1, 1) == 1

print("All unit tests are passed.")

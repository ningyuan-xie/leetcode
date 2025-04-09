"""1550. Three Consecutive Odds
Link: https://leetcode.com/problems/three-consecutive-odds/
Difficulty: Easy
Description: Given an integer array arr, return true if there are three consecutive odd numbers
in the array. Otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def threeConsecutiveOdds(arr: List[int]) -> bool:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the count of consecutive odd numbers
        count_of_consecutive_odds = 0

        # Iterate through the array
        for num in arr:
            # If the number is odd
            if num % 2:
                count_of_consecutive_odds += 1  # Increment the count of consecutive odd numbers
            else:
                count_of_consecutive_odds = 0  # Reset the count of consecutive odd numbers

            # If we've found three consecutive odd numbers
            if count_of_consecutive_odds == 3:
                return True

        return False


# Unit Test: arr = [2, 6, 4, 1], Output: False
assert Solution.threeConsecutiveOdds([2, 6, 4, 1]) is False

# Unit Test: arr = [1, 2, 34, 3, 4, 5, 7, 23, 12], Output: True
assert Solution.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]) is True

print("All unit tests are passed.")

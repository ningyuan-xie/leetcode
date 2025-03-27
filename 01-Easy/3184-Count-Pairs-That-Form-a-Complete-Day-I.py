"""3184. Count Pairs That Form a Complete Day I
Link: https://leetcode-cn.com/problems/Count-Pairs-That-Form-a-Complete-Day-I
Difficulty: Easy
Description: Given an integer array hours representing times in hours, return an integer
denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.
A complete day is defined as a time duration that is an exact multiple of 24 hours.
For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on."""

from typing import List


class Solution:
    @staticmethod
    def countCompleteDayPairs(hours: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 1. Two Sum"""
        # Initialize a dictionary to store the count of each remainder
        remainder_dict = {}

        count = 0
        # Iterate through the list of hours
        for hour in hours:
            remainder = hour % 24
            # Calculate the difference between the remainder and 24
            diff = 24 - remainder if remainder != 0 else 0
            print(hour, diff)

            # If the difference is in the dictionary, add the count of the difference to the total count
            if diff in remainder_dict:
                count += remainder_dict[diff]
            remainder_dict[remainder] = remainder_dict.get(remainder, 0) + 1

        # Return the total count of pairs
        return count


# Unit Test: hours = [12,12,30,24,24], Output = 2
assert Solution.countCompleteDayPairs([12, 12, 30, 24, 24]) == 2

# Unit Test: hours = [72,48,24,3], Output = 3
assert Solution.countCompleteDayPairs([72, 48, 24, 3]) == 3

print("All unit tests are passed")

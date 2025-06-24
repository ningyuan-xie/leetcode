"""1539. Kth Missing Positive Number
Link: https://leetcode.com/problems/kth-missing-positive-number/
Difficulty: Easy
Description: Given an array arr of positive integers sorted in a strictly increasing order, and
an integer k.
Return the kth positive integer that is missing from this array."""

from typing import List


class Solution:
    @staticmethod
    def findKthPositive(arr: List[int], k: int) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the count of missing numbers and the previous number in sequence
        count_of_missing, prev_num_in_sequence = 0, 0

        # Iterate through the array
        for current_num in arr:  # E.g. arr = [2, 3, 4, 7, 11]
            # Calculate the number of missing numbers between the previous and current number
            count_of_missing += (current_num - prev_num_in_sequence - 1)

            # If we've found at least 'k' missing numbers
            if count_of_missing >= k:
                # The k-th missing number lies between 'prev' and 'num'
                return current_num - (count_of_missing - k + 1)

            prev_num_in_sequence = current_num  # Update the previous number to the current one

        # If we haven't found the k-th missing number within the array,
        # the k-th missing number is greater than the last number in the array
        return arr[-1] + (k - count_of_missing)


# Input: arr = [2, 3, 4, 7, 11], k = 5, Output: 9
# Explanation: The missing numbers are [1, 5, 6, 8, 9, 10, ...], hence the 5th missing number is 9
assert Solution.findKthPositive([2, 3, 4, 7, 11], 5) == 9

# Input: arr = [1, 2, 3, 4], k = 2, Output: 6
# Explanation: The missing numbers are [5, 6, 7, ...], hence the 2nd missing number is 6
assert Solution.findKthPositive([1, 2, 3, 4], 2) == 6

print("All unit tests are passed.")

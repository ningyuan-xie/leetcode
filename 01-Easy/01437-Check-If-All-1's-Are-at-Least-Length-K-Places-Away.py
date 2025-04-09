"""1437. Check If All 1's Are at Least Length K Places Away
Link: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
Difficulty: Easy
Description: Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k
places away from each other, otherwise return False."""

from typing import List


class Solution:
    @staticmethod
    def kLengthApart(nums: List[int], k: int) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize last 1's index to -k - 1, so that the distance check below
        # i - last_one_index > k will always pass for the first 1 at index 0
        last_one_index = -k - 1

        # Iterate through the list to check the distance between 1's
        for i, num in enumerate(nums):
            # If the number is 1, check if the distance is at least k
            if num == 1:
                if i - last_one_index <= k:
                    return False
                # Update the index of the last 1
                last_one_index = i

        return True


# Unit Test: nums = [1, 0, 0, 0, 1, 0, 0, 1], k = 2, Output: True
assert Solution.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2) == True

# Unit Test: nums = [1, 0, 0, 1, 0, 1], k = 2, Output: False
assert Solution.kLengthApart([1, 0, 0, 1, 0, 1], 2) == False

# Unit Test: nums = [1, 1, 1, 1, 1], k = 0, Output: True
assert Solution.kLengthApart([1, 1, 1, 1, 1], 0) == True

# Unit Test: nums = [0, 1, 0, 1], k = 1, Output: True
assert Solution.kLengthApart([0, 1, 0, 1], 1) == True

print("All unit tests are passed.")

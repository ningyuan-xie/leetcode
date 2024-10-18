"""1502. Can Make Arithmetic Progression From Sequence
Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence
Difficulty: Easy
Description: A sequence of numbers is called an arithmetic progression if the difference between
any two consecutive elements is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic
progression. Otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def canMakeArithmeticProgression(arr: List[int]) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)"""
        # Sort the array
        arr.sort()

        # Calculate the difference
        diff = arr[1] - arr[0]

        # Iterate through the range of the array
        for i in range(1, len(arr)):
            # Check if the difference is not the same
            if arr[i] - arr[i - 1] != diff:
                return False

        return True


# Unit Test: arr = [3, 5, 1], Output: True
assert Solution.canMakeArithmeticProgression([3, 5, 1]) == True

# Unit Test: arr = [1, 2, 4], Output: False
assert Solution.canMakeArithmeticProgression([1, 2, 4]) == False

# Unit Test: arr = [1, 2, 3], Output: True
assert Solution.canMakeArithmeticProgression([1, 2, 3]) == True

# Unit Test: arr = [1, 2, 4, 5], Output: False
assert Solution.canMakeArithmeticProgression([1, 2, 4, 5]) == False

print("All unit tests are passed")

"""1089. Duplicate Zeros
Link: https://leetcode.com/problems/duplicate-zeros/
Difficulty: Easy
Description: Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the
remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications
to the input array in place, do not return anything, and modify the input array instead."""

from typing import List


class Solution:
    @staticmethod
    def duplicateZeros(arr: List[int]) -> None:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Count the number of zeros in the array
        zero_count = arr.count(0)

        # Initialize two index pointers: end of the original array and end of the modified array
        original_end = len(arr) - 1  # Last index of the original array
        modified_end = original_end + zero_count  # Where the last element would go if enough space

        # Shift elements and duplicate zeros
        while original_end >= 0:
            if modified_end < len(arr):
                # The first zero is placed by copying the value from original_end to modified_end
                arr[modified_end] = arr[original_end]

            # If it's a zero, duplicate it
            if arr[original_end] == 0:
                # Prepare to place the second zero right before the first zero
                modified_end -= 1
                if modified_end < len(arr):
                    # Actually place the second duplicate zero right before the first zero
                    arr[modified_end] = 0

            original_end -= 1
            modified_end -= 1


# Unit Test: arr = [1, 0, 2, 3, 0, 4, 5, 0], Output: [1, 0, 0, 2, 3, 0, 0, 4]
arr_test = [1, 0, 2, 3, 0, 4, 5, 0]
Solution.duplicateZeros(arr_test)
assert arr_test == [1, 0, 0, 2, 3, 0, 0, 4]

# Unit Test: arr = [1, 2, 3], Output: [1, 2, 3]
arr_test = [1, 2, 3]
Solution.duplicateZeros(arr_test)
assert arr_test == [1, 2, 3]

# Unit Test: arr = [0, 0, 0, 0, 0, 0, 0], Output: [0, 0, 0, 0, 0, 0, 0]
arr_test = [0, 0, 0, 0, 0, 0, 0]
Solution.duplicateZeros(arr_test)
assert arr_test == [0, 0, 0, 0, 0, 0, 0]

print("All unit tests are passed.")

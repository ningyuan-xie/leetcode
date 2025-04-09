"""1299. Replace Elements with Greatest Element on Right Side
Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Difficulty: Easy
Description: Given an array arr, replace every element in that array with the greatest element among the
elements to its right, and replace the last element with -1.
After doing so, return the array."""

from typing import List


class Solution:
    @staticmethod
    def replaceElements(arr: List[int]) -> List[int]:
        """Optimal Solution: Reverse Iteration. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the maximum value as -1
        max_value = -1

        # Traverse the array in reverse order
        for i in range(len(arr) - 1, -1, -1):
            # max_value is updated to the maximum of its current value and the original value
            # of arr[i] (before it was replaced)
            arr[i], max_value = max_value, max(max_value, arr[i])

        return arr


# Unit Test: arr = [17, 18, 5, 4, 6, 1], Output: [18, 6, 6, 6, 1, -1]
assert Solution.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]

# Unit Test: arr = [400], Output: [-1]
assert Solution.replaceElements([400]) == [-1]

# Unit Test: arr = [1, 2, 3, 4, 5], Output: [5, 5, 5, 5, -1]
assert Solution.replaceElements([1, 2, 3, 4, 5]) == [5, 5, 5, 5, -1]

print("All unit tests are passed.")

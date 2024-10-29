"""1619. Mean of Array After Removing Some Elements
Link: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
Difficulty: Easy
Description: Given an integer array arr, return the mean of the remaining integers after removing
the smallest 5% and the largest 5% of the elements.
Answers within 10^-5 of the actual answer will be considered accepted."""

from typing import List


class Solution:
    @staticmethod
    def trimMean(arr: List[int]) -> float:
        """Optimal Solution: Sorting. Time Complexity: O(nlogn), Space Complexity: O(1)"""
        # Sort the array in ascending order
        arr.sort()

        # Calculate the number of elements to remove from the smallest and largest 5%
        remove_count = 1 if len(arr) < 20 else len(arr) // 20

        # Calculate the sum of the remaining elements
        sum_remaining = sum(arr[remove_count:len(arr) - remove_count])

        # Calculate the mean of the remaining elements
        return sum_remaining / (len(arr) - 2 * remove_count)


# Unit Test: arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], Output: 2.00000
assert Solution.trimMean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == 2.00000

# Unit Test: arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], Output: 1.00000
assert Solution.trimMean([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1.00000

# Unit Test: arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0], Output: 4.00000
assert Solution.trimMean([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]) == 4.00000

print("All unit tests are passed")

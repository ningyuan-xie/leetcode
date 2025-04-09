"""1200. Minimum Absolute Difference
Link: https://leetcode.com/problems/minimum-absolute-difference/
Difficulty: Easy
Description: Given an array of distinct integers arr, find all pairs of elements with the minimum
absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr"""

from typing import List


class Solution:
    @staticmethod
    def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        # Sort the array in ascending order
        arr.sort()  # E.g. [4, 2, 1, 3] -> [1, 2, 3, 4]

        # Initialize the minimum absolute difference
        min_diff = float("inf")

        # Update the minimum absolute difference
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        # Find all pairs of elements with the minimum absolute difference
        result = [[arr[i - 1], arr[i]]
                  for i in range(1, len(arr))
                  if arr[i] - arr[i - 1] == min_diff]

        return result


# Unit Test: arr = [4, 2, 1, 3], Output: [[1, 2], [2, 3], [3, 4]]
assert Solution.minimumAbsDifference([4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]

# Unit Test: arr = [1, 3, 6, 10, 15], Output: [[1, 3]]
assert Solution.minimumAbsDifference([1, 3, 6, 10, 15]) == [[1, 3]]

# Unit Test: arr = [3, 8, -10, 23, 19, -4, -14, 27], Output: [[-14, -10], [19, 23], [23, 27]]
assert (Solution.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27])
        == [[-14, -10], [19, 23], [23, 27]])

print("All unit tests are passed.")

"""1331. Rank Transform of an Array
Link: https://leetcode.com/problems/rank-transform-of-an-array/
Difficulty: Easy
Description: Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
- Rank should be as small as possible."""

from typing import List


class Solution:
    @staticmethod
    def arrayRankTransform(arr: List[int]) -> List[int]:
        """Optimal Solution: Sort the array and create a dictionary to store the rank of each element.
           Time Complexity: O(nlog(n)), Space Complexity: O(n)"""
        rank = {}

        # Create sorted version of arr with unique values
        sorted_unique_arr = sorted(set(arr))  # E.g. [40, 10, 20, 30] -> [10, 20, 30, 40]

        # Assign ranks based on the sorted unique values
        for i, num in enumerate(sorted_unique_arr):
            rank[num] = i + 1

        # Replace each element in the original array with its rank
        return [rank[num] for num in arr]


# Unit Test: arr = [40, 10, 20, 30], Output: [4, 1, 2, 3]
assert Solution.arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]

# Unit Test: arr = [100, 100, 100], Output: [1, 1, 1]
assert Solution.arrayRankTransform([100, 100, 100]) == [1, 1, 1]

# Unit Test: arr = [37, 12, 28, 9, 100, 56, 80, 5, 12], Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]
assert Solution.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]) == [5, 3, 4, 2, 8, 6, 7, 1, 3]

print("All unit tests are passed.")

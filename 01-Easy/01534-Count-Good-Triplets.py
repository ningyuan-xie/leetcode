"""1534. Count Good Triplets
Link: https://leetcode.com/problems/count-good-triplets/
Difficulty: Easy
Description: Given an array of integers arr, and three integers a, b and c. You need to find the
number of good triplets.
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
- 0 <= i < j < k < arr.length
- |arr[i] - arr[j]| <= a
- |arr[j] - arr[k]| <= b
- |arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.
Return the number of good triplets."""

from typing import List


class Solution:
    @staticmethod
    def countGoodTriplets(arr: List[int], a: int, b: int, c: int) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^3), Space Complexity: O(1)"""
        # Initialize the count of good triplets
        count = 0

        # Iterate through all possible triplets
        for i in range(len(arr)):  # i = 0, 1, 2
            for j in range(i + 1, len(arr)):  # j = 1, 2
                for k in range(j + 1, len(arr)):  # k = 2
                    # Check if the triplet is good
                    if (abs(arr[i] - arr[j]) <= a
                            and abs(arr[j] - arr[k]) <= b
                            and abs(arr[i] - arr[k]) <= c):
                        count += 1

        return count


# Unit Test: arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3, Output: 4
assert Solution.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3) == 4

# Unit Test: arr = [1, 1, 2, 2, 3], a = 0, b = 0, c = 1, Output: 0
assert Solution.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1) == 0

# Unit Test: arr = [7, 3, 7, 3, 12, 1, 12, 2, 3], a = 5, b = 8, c = 1, Output: 12
assert Solution.countGoodTriplets([7, 3, 7, 3, 12, 1, 12, 2, 3], 5, 8, 1) == 12

print("All unit tests are passed")

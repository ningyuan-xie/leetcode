"""1385. Find the Distance Value Between Two Arrays
Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
Difficulty: Easy
Description: Given two integer arrays arr1 and arr2, and the integer d, return the distance value
between the two arrays.
The distance value is defined as the number of elements arr1[i] such that there is not any element
arr2[j] where |arr1[i]-arr2[j]| <= d."""

from typing import List


class Solution:
    @staticmethod
    def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(1)"""
        count = 0
        for x in arr1:
            # Check if for every element y in arr2, the condition |x - y| > d holds
            if all(abs(x - y) > d for y in arr2):
                count += 1
        return count


# Unit Test: arr1 = [4, 5, 8], arr2 = [10, 9, 1, 8], d = 2, Output: 2
assert Solution.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2) == 2

# Unit Test: arr1 = [1, 4, 2, 3], arr2 = [-4, -3, 6, 10, 20, 30], d = 3, Output: 2
assert Solution.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3) == 2

# Unit Test: arr1 = [2, 1, 100, 3], arr2 = [-5, -2, 10, -3, 7], d = 6, Output: 1
assert Solution.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6) == 1

print("All unit tests are passed.")

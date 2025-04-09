"""1356. Sort Integers by The Number of 1 Bits
Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
Difficulty: Easy
Description: You are given an integer array arr. Sort the integers in the array in ascending order
by the number of 1's in their binary representation and in case of two or more integers have the
same number of 1's you have to sort them in ascending order.
Return the array after sorting it."""

from typing import List


class Solution:
    @staticmethod
    def sortByBits(arr: List[int]) -> List[int]:
        """Optimal Solution: Sorting with lambda function.
           Time Complexity: O(nlog(n)), Space Complexity: O(n)."""
        # Sort the array based on the number of 1's in the binary representation of each element
        # key=lambda x: (bin(x).count("1"), x) sorts by the number of 1's and then by the element itself
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


# Unit Test: arr = [0, 1, 2, 3, 4, 5, 6, 7, 8], Output: [0, 1, 2, 4, 8, 3, 5, 6, 7]
assert Solution.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]

# Unit Test: arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
assert (Solution.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
        == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])

# Unit Test: arr = [10000, 10000], Output: [10000, 10000]
assert Solution.sortByBits([10000, 10000]) == [10000, 10000]

# Unit Test: arr = [2, 3, 5, 7, 11, 13, 17, 19], Output: [2, 3, 5, 17, 7, 11, 13, 19]
assert Solution.sortByBits([2, 3, 5, 7, 11, 13, 17, 19]) == [2, 3, 5, 17, 7, 11, 13, 19]

print("All unit tests are passed.")

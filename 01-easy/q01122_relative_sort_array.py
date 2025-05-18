"""1122. Relative Sort Array
Link: https://leetcode.com/problems/relative-sort-array/
Difficulty: Easy
Description: Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in
arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order."""

from typing import List


class Solution:
    @staticmethod
    def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
        """Optimal Solution: Sort by Custom Order. Time Complexity: O(n), Space Complexity: O(n)."""
        # Count the occurrences of each element in arr1
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1  # {2: 3, 3: 2, 1: 1, 4: 1, 6: 1, 7: 1, 9: 1, 19: 1}

        # Initialize the sorted array
        sorted_arr = []

        # Sort the elements in arr1 based on the order in arr2
        for num in arr2:
            sorted_arr.extend([num] * count[num])  # [2, 2, 2, 1, 4, 3, 3, 9, 6]
            count.pop(num)  # .pop() removes the key from the dictionary; left with {7: 1, 19: 1}

        # Sort the remaining elements in arr1 that are not in arr2
        for num in sorted(count.keys()):
            sorted_arr.extend([num] * count[num])

        return sorted_arr


# Unit Test: arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2 = [2, 1, 4, 3, 9, 6],
# Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
assert Solution.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
                                  [2, 1, 4, 3, 9, 6]) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

# Unit Test: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6], Output: [22, 28, 8, 6, 17, 44]
assert Solution.relativeSortArray([28, 6, 22, 8, 44, 17],
                                  [22, 28, 8, 6]) == [22, 28, 8, 6, 17, 44]

print("All unit tests are passed.")

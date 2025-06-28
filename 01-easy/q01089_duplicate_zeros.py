"""1089. Duplicate Zeros
Link: https://leetcode.com/problems/duplicate-zeros/
Difficulty: Easy
Description: Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything."""

from typing import List


class Solution:
    @staticmethod
    def duplicateZeros(arr: List[int]) -> None:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(n)."""
        result = []
        for num in arr:
            if num == 0:
                result.extend([0, 0])
            else:
                result.append(num)

        for i in range(len(arr)):
            arr[i] = result[i]


def unit_tests():
    # Input: arr = [1, 0, 2, 3, 0, 4, 5, 0], Output: [1, 0, 0, 2, 3, 0, 0, 4]
    arr_test = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution.duplicateZeros(arr_test)
    assert arr_test == [1, 0, 0, 2, 3, 0, 0, 4]

    # Input: arr = [1, 2, 3], Output: [1, 2, 3]
    arr_test = [1, 2, 3]
    Solution.duplicateZeros(arr_test)
    assert arr_test == [1, 2, 3]

    # Input: arr = [0, 0, 0, 0, 0, 0, 0], Output: [0, 0, 0, 0, 0, 0, 0]
    arr_test = [0, 0, 0, 0, 0, 0, 0]
    Solution.duplicateZeros(arr_test)
    assert arr_test == [0, 0, 0, 0, 0, 0, 0]

    # Input: arr = [0, 1, 7, 6, 0, 2, 0, 7], Output: [0, 0, 1, 7, 6, 0, 0, 2]
    arr_test = [0, 1, 7, 6, 0, 2, 0, 7]
    Solution.duplicateZeros(arr_test)
    assert arr_test == [0, 0, 1, 7, 6, 0, 0, 2]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests passed!")

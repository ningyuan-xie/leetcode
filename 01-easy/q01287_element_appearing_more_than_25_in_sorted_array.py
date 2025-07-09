"""1287. Element Appearing More Than 25% In Sorted Array
Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
Difficulty: Easy
Description: Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer."""

from typing import List


class Solution:
    @staticmethod
    def findSpecialInteger(arr: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(arr) // 4:
                return num
        return -1


def unit_tests():
    # Input: arr = [1, 2, 2, 6, 6, 6, 6, 7, 10], Output: 6
    assert Solution.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6

    # Input: arr = [1, 1], Output: 1
    assert Solution.findSpecialInteger([1, 1]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

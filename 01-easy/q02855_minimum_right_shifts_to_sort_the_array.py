"""2855. Minimum Right Shifts to Sort the Array
Link: https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/
Difficulty: Easy
Description: You are given a 0-indexed array nums of length n containing distinct positive integers.
Return the minimum number of right shifts required to sort nums and -1 if this is not possible.
A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices."""

from typing import List


class Solution:
    @staticmethod
    def minimumRightShifts(nums: List[int]) -> int:
        """Optimal Solution: Drop Index. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(nums)

        # Check if already sorted
        if all(nums[i] < nums[i+1] for i in range(n-1)):
            return 0  # Already sorted

        # Find the index of the drop: the point where the array is not sorted
        drop_index = -1
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if drop_index != -1:
                    return -1  # More than one drop, not a valid rotation
                drop_index = i + 1  # The part at drop_index is rotated to the beginning

        # Check if after rotation, the array is sorted
        if drop_index == -1:
            return 0  # Already sorted
        if (all(nums[i] < nums[i+1] for i in range(drop_index, n-1))
                and nums[-1] < nums[0]):
            return n - drop_index  # Number of shifts required

        return -1  # Not possible


# Input: nums = [3,4,5,1,2], Output: 2
assert Solution.minimumRightShifts([3, 4, 5, 1, 2]) == 2

# Input: nums = [1,3,5], Output: 0
assert Solution.minimumRightShifts([1, 3, 5]) == 0

# Input: nums = [2,1,4], Output: -1
assert Solution.minimumRightShifts([2, 1, 4]) == -1

print("All unit tests are passed.")

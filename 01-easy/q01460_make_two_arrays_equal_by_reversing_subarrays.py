"""1460. Make Two Arrays Equal by Reversing Sub-arrays
Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
Difficulty: Easy
Description: You are given two integer arrays of equal length target and arr. In one step, you can
select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def canBeEqual(target: List[int], arr: List[int]) -> bool:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        # Sort the target and arr arrays
        target.sort()
        arr.sort()

        # Return True if the target and arr arrays are equal, otherwise return False
        return target == arr


# Unit Test: target = [1, 2, 3, 4], arr = [2, 4, 1, 3], Output: True
assert Solution.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]) is True

# Unit Test: target = [7], arr = [7], Output: True
assert Solution.canBeEqual([7], [7]) is True

# Unit Test: target = [1, 12], arr = [12, 1], Output: True
assert Solution.canBeEqual([1, 12], [12, 1]) is True

# Unit Test: target = [3, 7, 9], arr = [3, 7, 11], Output: False
assert Solution.canBeEqual([3, 7, 9], [3, 7, 11]) is False

# Unit Test: target = [1, 1, 1, 1, 1], arr = [1, 1, 1, 1, 1], Output: True
assert Solution.canBeEqual([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]) is True

print("All unit tests are passed.")

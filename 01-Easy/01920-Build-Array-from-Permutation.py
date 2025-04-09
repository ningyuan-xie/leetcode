"""1920. Build Array from Permutation
Link: https://leetcode.com/problems/build-array-from-permutation/
Difficulty: Easy
Description: Given a zero-based permutation nums (0-indexed), build an array ans of the same length
where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive)."""

from typing import List


class Solution:
    @staticmethod
    def buildArray(nums: List[int]) -> List[int]:
        """Optimal Solution: One Pass. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            ans[i] = nums[nums[i]]

        return ans


# Unit Test: nums = [0, 2, 1, 5, 3, 4], Output: [0, 1, 2, 4, 5, 3]
assert Solution.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]

# Unit Test: nums = [5, 0, 1, 2, 3, 4], Output: [4, 5, 0, 1, 2, 3]
assert Solution.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]

# Unit Test: nums = [0, 1, 2, 3, 4], Output: [0, 1, 2, 3, 4]
assert Solution.buildArray([0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4]

print("All unit tests are passed.")

"""2460. Apply Operations to an Array
Link: https://leetcode.com/problems/apply-operations-to-an-array/
Difficulty: Easy
Description: You are given a 0-indexed array nums of size n consisting of non-negative integers.
You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will
apply the following on the ith element of nums:
- If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip
this operation.
After performing all the operations, shift all the 0's to the end of the array.
- For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.
Note that the operations are applied sequentially, not all at once."""

from typing import List


class Solution:
    @staticmethod
    def applyOperations(nums: List[int]) -> List[int]:
        """Optimal Solution: Array. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        # E.g. [1, 2, 2, 1, 1, 0] -> [1, 4, 0, 2, 0, 0]

        # Shift all zeros to the end of the array
        result = n * [0]
        index = 0
        for i in range(n):
            if nums[i] != 0:
                result[index] = nums[i]
                index += 1
        return result


# Input: nums = [1,2,2,1,1,0], Output: [1,4,2,0,0,0]
assert Solution.applyOperations([1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]

# Input: nums = [0,1], Output: [1,0]
assert Solution.applyOperations([0, 1]) == [1, 0]

print("All unit tests are passed.")

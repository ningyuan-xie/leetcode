"""1389. Create Target Array in the Given Order
Link: https://leetcode.com/problems/create-target-array-in-the-given-order/
Difficulty: Easy
Description: Given two arrays of integers nums and index. Your task is to create target array under
the following rules:
- Initially target array is empty.
- From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target.
- Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid."""

from typing import List


class Solution:
    @staticmethod
    def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
        """Optimal Solution: .insert() method. Time Complexity: O(n), Space Complexity: O(n)."""
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


# Unit Test: nums = [0, 1, 2, 3, 4], index = [0, 1, 2, 2, 1], Output: [0, 4, 1, 3, 2]
assert Solution.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]) == [0, 4, 1, 3, 2]

# Unit Test: nums = [1, 2, 3, 4, 0], index = [0, 1, 2, 3, 0], Output: [0, 1, 2, 3, 4]
assert Solution.createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]) == [0, 1, 2, 3, 4]

# Unit Test: nums = [1], index = [0], Output: [1]
assert Solution.createTargetArray([1], [0]) == [1]

print("All unit tests are passed.")

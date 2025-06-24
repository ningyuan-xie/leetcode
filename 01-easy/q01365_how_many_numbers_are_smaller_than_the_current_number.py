"""1365. How Many Numbers Are Smaller Than the Current Number
Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Difficulty: Easy
Description: Given the array nums, for each nums[i] find out how many numbers in the array are
smaller than it. That is, for each nums[i] you have to count the number of valid j's such that
j != i and nums[j] < nums[i].
Return the answer in an array."""

from typing import List


class Solution:
    @staticmethod
    def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
        """Optimal Solution: Counting Sort. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 1051-Height-Checker.py"""
        count = [0] * 101

        # Count the frequency of each number in the array
        # E.g. [8, 1, 2, 2, 3] -> [0, 1, 2, 1, 0, 0, 0, 0, 1, 0, ..., 0]
        for num in nums:
            count[num] += 1

        # Update count to store the number of elements smaller than or equal to the current element
        # E.g. [0, 1, 2, 1, 0, 0, 0, 0, 1, 0, ..., 0] -> [0, 1, 3, 4, 4, 4, 4, 4, 5, 5, ..., 5]
        for i in range(1, 101):
            count[i] += count[i - 1]

        result = []

        # Return the result
        # E.g. [8, 1, 2, 2, 3] -> [0, 1, 3, 4, 4, 4, 4, 4, 5, 5, ..., 5] -> [4, 0, 1, 1, 3]
        for num in nums:
            result.append(count[num - 1] if num != 0 else 0)
        return result


# Input: nums = [8, 1, 2, 2, 3], Output: [4, 0, 1, 1, 3]
assert Solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]

# Input: nums = [6, 5, 4, 8], Output: [2, 1, 0, 3]
assert Solution.smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]

# Input: nums = [7, 7, 7, 7], Output: [0, 0, 0, 0]
assert Solution.smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]

print("All unit tests are passed.")

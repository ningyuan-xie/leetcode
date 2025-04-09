"""1991. Find the Middle Index in Array
Link: https://leetcode.com/problems/find-the-middle-index-in-array/
Difficulty: Easy
Description: Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest
amongst all the possible ones).
A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1]
+ nums[middleIndex+2] + ... + nums[nums.length-1].
If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex ==
nums.length - 1, the right side sum is considered to be 0.
Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index."""

from typing import List


class Solution:
    @staticmethod
    def findMiddleIndex(nums: List[int]) -> int:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1)"""
        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Initialize the left sum to 0
        left_sum = 0

        # Iterate through the array to find the middle index
        for i, num in enumerate(nums):
            # Check if the left sum is equal to the right sum
            if left_sum == total_sum - left_sum - num:
                return i

            # Update the left sum
            left_sum += num

        # If no middle index is found, return -1
        return -1


# Unit Test: nums = [2, 3, -1, 8, 4], Output: 3
assert Solution.findMiddleIndex([2, 3, -1, 8, 4]) == 3

# Unit Test: nums = [1, -1, 4], Output: 2
assert Solution.findMiddleIndex([1, -1, 4]) == 2

# Unit Test: nums = [2, 5], Output: -1
assert Solution.findMiddleIndex([2, 5]) == -1

print("All unit tests are passed.")

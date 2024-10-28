"""1608. Special Array With X Elements Greater Than or Equal X
Link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
Difficulty: Easy
Description: You are given an array nums of non-negative integers. nums is considered special if there
exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special,
the value for x is unique."""

from typing import List


class Solution:
    @staticmethod
    def specialArray(nums: List[int]) -> int:
        """Optimal Solution: Counting Sort. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the counting array with zeros
        count = [0] * (len(nums) + 1)  # E.g. nums = [3, 5] -> count = [0, 0, 0]

        # Count the frequency of each number capped at len(nums): grouping all out-of-bounds numbers
        # at count[len(nums)] simplifies the counting process and avoid excessively large count array
        for num in nums:
            count[min(num, len(nums))] += 1  # count[min(3, 2)] += 1, count[min(5, 2)] += 1

        # Initialize the total count of elements >= x
        greater_or_equal_count = 0

        # Iterate backward from the largest possible element len(nums) down to the smallest element 1
        for x in range(len(nums), 0, -1):  # range(2, 0, -1)
            greater_or_equal_count += count[x]

            # greater_or_equal_count increases while x decreases, until they meet
            if greater_or_equal_count == x:
                return x

        return -1


# Unit Test: nums = [3, 5], Output: 2
assert Solution.specialArray([3, 5]) == 2

# Unit Test: nums = [0, 0], Output: -1
assert Solution.specialArray([0, 0]) == -1

# Unit Test: nums = [0, 4, 3, 0, 4], Output: 3
# count = [0, 0, 0, 0, 0, 0] -> [2, 0, 0, 1, 2, 0], x in range(5, 0, -1) -> x = 3
assert Solution.specialArray([0, 4, 3, 0, 4]) == 3

print("All unit tests are passed")

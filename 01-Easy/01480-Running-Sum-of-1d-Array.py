"""1480. Running Sum of 1d Array
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Difficulty: Easy
Description: Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums."""

from typing import List


class Solution:
    @staticmethod
    def runningSum(nums: List[int]) -> List[int]:
        """Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the running sum array and the current sum
        running_sum, current_sum = [], 0

        # Iterate through the nums array
        for num in nums:
            # Add the num to the sum
            current_sum += num
            # Append the sum to the running sum array
            running_sum.append(current_sum)

        # Return the running sum array
        return running_sum


# Unit Test: nums = [1, 2, 3, 4], Output: [1, 3, 6, 10]
assert Solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]

# Unit Test: nums = [1, 1, 1, 1, 1], Output: [1, 2, 3, 4, 5]
assert Solution.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]

# Unit Test: nums = [3, 1, 2, 10, 1], Output: [3, 4, 6, 16, 17]
assert Solution.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]

print("All unit tests are passed.")

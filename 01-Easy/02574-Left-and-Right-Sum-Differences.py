"""2574. Left and Right Sum Differences
Link: https://leetcode.com/problems/left-and-right-sum-differences/
Difficulty: Easy
Description: Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
- answer.length == nums.length.
- answer[i] = |leftSum[i] - rightSum[i]|.
Where:
- leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no
such element, leftSum[i] = 0.
- rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no
such element, rightSum[i] = 0.
Return the array answer."""

from typing import List


class Solution:
    @staticmethod
    def leftRigthDifference(nums: List[int]) -> List[int]:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(n)"""
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        # Calculate leftSum for each index cumulatively
        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]

        # Calculate rightSum for each index cumulatively
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]

        # Calculate the absolute difference
        answer = [abs(left_sum[i] - right_sum[i]) for i in range(n)]
        return answer


# Unit Test: nums = [10,4,8,3], Output: [15,1,11,22]
assert Solution.leftRigthDifference([10, 4, 8, 3]) == [15, 1, 11, 22]

# Unit Test: nums = [1], Output: [0]
assert Solution.leftRigthDifference([1]) == [0]

print("All unit tests are passed.")

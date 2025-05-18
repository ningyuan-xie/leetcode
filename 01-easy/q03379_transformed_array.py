"""3379. Transformed Array
Link: https://leetcode.com/problems/transformed-array/
Difficulty: Easy
Description: You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:
For each index i (where 0 <= i < nums.length), perform the following independent actions:
• If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
• If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
• If nums[i] == 0: Set result[i] to nums[i].
Return the new array result.
Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end."""

from typing import List


class Solution:
    @staticmethod
    def constructTransformedArray(nums: List[int]) -> List[int]:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(nums)
        result = [0] * n

        for i in range(n):
            index = (i + nums[i]) % n
            result[i] = nums[index]
        return result


def unit_tests():
    # Input: nums = [3,-2,1,1], Output: [1,1,1,3]
    assert Solution.constructTransformedArray([3, -2, 1, 1]) == [1, 1, 1, 3]

    # Input: nums = [-1,4,-1], Output: [-1,-1,4]
    assert Solution.constructTransformedArray([-1, 4, -1]) == [-1, -1, 4]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

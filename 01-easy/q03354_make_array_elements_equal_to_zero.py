"""3354. Make Array Elements Equal to Zero
Link: https://leetcode.com/problems/make-array-elements-equal-to-zero/
Difficulty: Easy
Description: You are given an integer array nums.
Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.
After that, you repeat the following process:
- If curr is out of the range [0, n - 1], this process ends.
- If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
- Else if nums[curr] > 0:
-- Decrement nums[curr] by 1.
-- Reverse your movement direction (left becomes right and vice versa).
-- Take a step in your new direction.
A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.
Return the number of possible valid selections."""

from typing import List


class Solution:
    def countValidSelections(nums: List[int]) -> int:
        """Optimal Solution: Prefix and Suffix Sums. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(nums)

        # Precompute using n+1 to handle edge cases, which won't affect prefix and suffix sums
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        suffix_sum = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + nums[i]

        count = 0
        for i in range(n):
            if nums[i] == 0:
                diff_left = prefix_sum[i] - suffix_sum[i+1]
                diff_right = suffix_sum[i+1] - prefix_sum[i]
                # Check if going left is valid
                if diff_left == 0 or diff_left == 1:
                    count += 1
                # Check if going right is valid
                if diff_right == 0 or diff_right == 1:
                    count += 1
        return count


def unit_tests():
    # Input: nums = [1,0,2,0,3], Output: 2
    assert Solution.countValidSelections([1, 0, 2, 0, 3]) == 2

    # Input: nums = [2,3,4,0,4,1,0], Output: 0
    assert Solution.countValidSelections([2, 3, 4, 0, 4, 1, 0]) == 0

    # Input: nums = [16,13,10,0,0,0,10,6,7,8,7], Output: 3
    assert Solution.countValidSelections([16, 13, 10, 0, 0, 0, 10, 6, 7, 8, 7]) == 3

    # Input: nums = [0], Output: 2
    assert Solution.countValidSelections([0]) == 2

    # Input: nums = [0,1], Output: 1
    assert Solution.countValidSelections([0, 1]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

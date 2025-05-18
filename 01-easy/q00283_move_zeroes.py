"""283. Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy
Description: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Follow up: Could you minimize the total number of operations done?"""

from typing import List


class Solution:
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize a pointer for the position of the last non-zero element
        last_non_zero_index = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not zero, move it to the last non-zero position
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

        # Fill the remaining positions with zeros
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0


def unit_tests():
    # Input: nums = [0,1,0,3,12], Output: [1,3,12,0,0]
    nums_test = [0, 1, 0, 3, 12]
    Solution.moveZeroes(nums_test)
    assert nums_test == [1, 3, 12, 0, 0]

    # Input: nums = [0], Output: [0]
    nums_test = [0]
    Solution.moveZeroes(nums_test)
    assert nums_test == [0]

    # Input: nums = [0,0,0,0,0], Output: [0,0,0,0,0]
    nums_test = [0, 0, 0, 0, 0]
    Solution.moveZeroes(nums_test)
    assert nums_test == [0, 0, 0, 0, 0]

    # Input: nums = [1,0,2,3,4,5], Output: [1,2,3,4,5,0]
    nums_test = [1, 0, 2, 3, 4, 5]
    Solution.moveZeroes(nums_test)
    assert nums_test == [1, 2, 3, 4, 5, 0]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

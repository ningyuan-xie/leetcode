"""485. Max Consecutive Ones
Link: https://leetcode.com/problems/max-consecutive-ones/
Difficulty: Easy
Description: Given a binary array, find the maximum number of consecutive 1s in this array."""

from typing import List


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the maximum count and current count
        max_count = 0
        current_count = 0

        # Iterate through the array
        for num in nums:
            if num == 1:
                # Increment the current count if the number is 1
                current_count += 1
            else:
                # Update the maximum count if the current count is greater
                max_count = max(max_count, current_count)
                # Reset the current count
                current_count = 0

        # Final check to update max_count in case the last element was 1
        return max(max_count, current_count)


def unit_tests():
    # Input: [1, 1, 0, 1, 1, 1], Output: 3
    assert Solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3

    # Input: [1, 0, 1, 1, 0, 1], Output: 2
    assert Solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2

    # Input: [1, 1, 1, 1, 1, 1], Output: 6
    assert Solution.findMaxConsecutiveOnes([1, 1, 1, 1, 1, 1]) == 6


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

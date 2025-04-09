"""3349. Adjacent Increasing Subarrays Detection I
Link: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/
Difficulty: Easy
Description: Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
- Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
- The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def hasIncreasingSubarrays(nums: List[int], k: int) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n * k), Space Complexity: O(1)."""
        # Iterate through the array and check for adjacent increasing subarrays
        for i in range(len(nums) - 2 * k + 1):
            # Check if both subarrays are strictly increasing
            if all(nums[j] < nums[j + 1] for j in range(i, i + k - 1)) and \
               all(nums[j] < nums[j + 1] for j in range(i + k, i + 2 * k - 1)):
                return True

        return False


def unit_tests():
    # Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3, Output: true
    assert Solution.hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3) is True

    # Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5, Output: false
    assert Solution.hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

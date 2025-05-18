"""3507. Minimum Pair Removal to Sort Array I
Link: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
Difficulty: Easy
Description: Given an array nums, you can perform the following operation any number of times:
• Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
• Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.
An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists)."""

from typing import List


class Solution:
    @staticmethod
    def minimumPairRemoval(nums: List[int]) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(n^2), Space Complexity: O(1)."""
        # Initialize the number of operations to 0
        operations = 0

        # While the array is not non-decreasing
        while True:
            # Check if already non-decreasing
            if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
                return operations

            # Find the leftmost adjacent pair with minimum sum
            min_sum = float('inf')
            min_index = -1
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i

            # Merge the pair at min_index
            nums[min_index] = nums[min_index] + nums[min_index + 1]
            nums.pop(min_index + 1)
            operations += 1


def unit_tests():
    # Input: nums = [5,2,3,1], Output: 2
    assert Solution.minimumPairRemoval([5, 2, 3, 1]) == 2

    # Input: nums = [1,2,2], Output: 0
    assert Solution.minimumPairRemoval([1, 2, 2]) == 0

    # Input: nums = [2,2,-1,3,-2,2,1,1,1,0,-1], Output: 9
    assert Solution.minimumPairRemoval([2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1]) == 9


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

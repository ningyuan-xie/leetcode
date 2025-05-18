"""2210. Count Hills and Valleys in an Array
Link: https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums. An index i is part of a hill in nums
if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of
a valley in nums if the closest non-equal neighbors of i are larger than nums[i].
Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].
Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both
the left and right of the index.
Return the number of hills and valleys in nums."""

from typing import List


class Solution:
    @staticmethod
    def countHillsAndValleys(nums: List[int]) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(nums)
        count = 0

        # Iterate through the array, skipping the first and last index
        for i in range(1, n - 1):
            # Skip duplicates to find the closest non-equal neighbors
            if nums[i] == nums[i - 1]:
                continue

            # Find the closest non-equal right neighbor
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1

            # Ensure valid neighbors exist
            if j < n:
                # Check for hill
                if nums[i] > nums[i - 1] and nums[i] > nums[j]:
                    count += 1
                # Check for valley
                elif nums[i] < nums[i - 1] and nums[i] < nums[j]:
                    count += 1

        return count


# Unit Test: nums = [2,4,1,1,6,5], Output: 3
assert Solution.countHillsAndValleys([2, 4, 1, 1, 6, 5]) == 3

# Unit Test: nums = [6,6,5,5,4,1], Output: 0
assert Solution.countHillsAndValleys([6, 6, 5, 5, 4, 1]) == 0

print("All unit tests are passed.")

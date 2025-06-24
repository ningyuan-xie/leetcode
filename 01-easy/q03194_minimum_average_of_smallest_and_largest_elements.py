"""3194. Minimum Average of Smallest and Largest Elements
Link: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements
Difficulty: Easy
Description: You have an array of floating point numbers averages which is initially empty. You
are given an array nums of n integers where n is even.
You repeat the following procedure n / 2 times:
- Remove the smallest element, minElement, and the largest element maxElement, from nums.
- Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages."""

from typing import List


class Solution:
    @staticmethod
    def minimumAverage(nums: List[int]) -> float:
        """Optimal Solution: Sorting. Time Complexity: O(nlogn), Space Complexity: O(1)."""
        # Sort the list of numbers
        nums.sort()

        # Initialize the minimum average
        min_avg = float("inf")

        # Iterate through the list of numbers
        for i in range(len(nums) // 2):
            # Calculate the average of the smallest and largest elements
            avg = (nums[i] + nums[-i - 1]) / 2

            # Update the minimum average
            min_avg = min(min_avg, avg)

        # Return the minimum average
        return min_avg


# Input: nums = [7,8,3,4,15,13,4,1], Output = 5.5
assert Solution.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]) == 5.5

# Input: nums = [1,9,8,3,10,5], Output = 5.5
assert Solution.minimumAverage([1, 9, 8, 3, 10, 5]) == 5.5

# Input: nums = [1,2,3,7,8,9], Output = 5.0
assert Solution.minimumAverage([1, 2, 3, 7, 8, 9]) == 5.0

print("All unit tests are passed.")

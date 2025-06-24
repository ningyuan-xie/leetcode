"""2465. Number of Distinct Averages
Link: https://leetcode.com/problems/number-of-distinct-averages/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums of even length.
As long as nums is not empty, you must repetitively:
- Find the minimum number in nums and remove it.
- Find the maximum number in nums and remove it.
- Calculate the average of the two removed numbers.
The average of two numbers a and b is (a + b) / 2.
- For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
Return the number of distinct averages calculated using the above process.
Note that when there is a tie for a minimum or maximum number, any can be removed."""

from typing import List


class Solution:
    @staticmethod
    def distinctAverages(nums: List[int]) -> int:
        """Optimal Solution: Hash Set. Time Complexity: O(nlogn), Space Complexity: O(n)."""
        nums.sort()  # E.g. [4, 1, 4, 0, 3, 5] -> [0, 1, 3, 4, 4, 5]
        n = len(nums)
        distinct_averages = set()

        # Calculate the average of the minimum and maximum numbers; only loop through half of the array
        for i in range(n // 2):
            average = (nums[i] + nums[n - i - 1]) / 2
            distinct_averages.add(average)
        return len(distinct_averages)


# Input: nums = [4,1,4,0,3,5], Output: 2
assert Solution.distinctAverages([4, 1, 4, 0, 3, 5]) == 2

# Input: nums = [1,1000000], Output: 1
assert Solution.distinctAverages([1, 1000000]) == 1

print("All unit tests are passed.")

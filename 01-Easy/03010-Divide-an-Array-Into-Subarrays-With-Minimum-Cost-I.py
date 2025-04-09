"""3010. Divide an Array Into Subarrays With Minimum Cost
Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost/
Difficulty: Easy
Description: ou are given an array of integers nums of length n.
The cost of an array is the value of its first element. For example, the cost of [1,2,3]
is 1 while the cost of [3,4,1] is 3.
You need to divide nums into 3 disjoint contiguous subarrays.
Return the minimum possible sum of the cost of these subarrays."""

from typing import List


class Solution:
    @staticmethod
    def minimumCost(nums: List[int]) -> int:
        """Optimal Solution: Find the 2 smallest elements.
           Time Complexity: O(n), Space Complexity: O(1)"""
        first, second = float("inf"), float("inf")
        n = len(nums)

        # Find the 2 smallest elements in the range of 1 to n
        for i in range(1, n):
            if nums[i] < first:
                first, second = nums[i], first
            elif nums[i] < second:
                second = nums[i]
        return nums[0] + first + second


# Unit Test: nums = [1,2,3,12], Output = 6
assert Solution.minimumCost([1, 2, 3, 12]) == 6

# Unit Test: nums = [5,4,3], Output = 12
assert Solution.minimumCost([5, 4, 3]) == 12

# Unit Test: nums = [10,3,1,1], Output = 12
assert Solution.minimumCost([10, 3, 1, 1]) == 12

print("All unit tests are passed.")

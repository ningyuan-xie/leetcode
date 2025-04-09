"""3028. Ant on the Boundary
Link: https://leetcode.com/problems/ant-on-the-boundary/
Difficulty: Easy
Description: An ant is on a boundary. It sometimes goes left and sometimes right.
You are given an array of non-zero integers nums. The ant starts reading nums from the
first element of it to its end. At each step, it moves according to the value of the
current element:
- If nums[i] < 0, it moves left by -nums[i] units.
- If nums[i] > 0, it moves right by nums[i] units.
Return the number of times the ant returns to the boundary.
Notes:
- There is an infinite space on both sides of the boundary.
- We check whether the ant is on the boundary only after it has moved |nums[i]| units.
In other words, if the ant crosses the boundary during its movement, it does not count."""

from typing import List


class Solution:
    @staticmethod
    def returnToBoundaryCount(nums: List[int]) -> int:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the number of times the ant returns to the boundary
        n = len(nums)
        boundary_count = 0
        prefix_sum = 0

        # Iterate through the array and count the number of times the ant returns
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum == 0:
                boundary_count += 1

        return boundary_count


# Unit Test: nums = [2,3,-5], Output = 1
assert Solution.returnToBoundaryCount([2, 3, -5]) == 1

# Unit Test: nums = [3,2,-3,-4], Output = 0
assert Solution.returnToBoundaryCount([3, 2, -3, -4]) == 0

print("All unit tests are passed.")

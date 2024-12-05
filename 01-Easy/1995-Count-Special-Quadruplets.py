"""1995. Count Special Quadruplets
Link: https://leetcode.com/problems/count-special-quadruplets/
Difficulty: Easy
Description: Given a 0-indexed integer array nums, return the number of distinct quadruplets
(a, b, c, d) such that:
- nums[a] + nums[b] + nums[c] == nums[d], and
- a < b < c < d"""

from typing import List


class Solution:
    @staticmethod
    def countQuadruplets(nums: List[int]) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n^4), Space Complexity: O(1)"""
        # Initialize the count of special quadruplets
        count = 0

        # Iterate through all possible quadruplets
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        # If the quadruplet satisfies the condition, increment the count
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1

        return count


# Unit Test: nums = [1, 2, 3, 6], Output: 1
assert Solution.countQuadruplets([1, 2, 3, 6]) == 1

# Unit Test: nums = [3, 3, 6, 4, 5], Output: 0
assert Solution.countQuadruplets([3, 3, 6, 4, 5]) == 0

# Unit Test: nums = [1, 1, 1, 3, 5], Output: 4
assert Solution.countQuadruplets([1, 1, 1, 3, 5]) == 4

# Unit Test: nums = [56,50,33,1,86,80,85,42,90], Output: 1
assert Solution.countQuadruplets([56, 50, 33, 1, 86, 80, 85, 42, 90]) == 1

print("All unit tests are passed")

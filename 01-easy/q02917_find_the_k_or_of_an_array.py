"""2917. Find the K-th or of an Array
Link: https://leetcode.com/problems/find-the-kth-or-of-an-array/
Difficulty: Easy
Description: You are given an integer array nums, and an integer k. Let's introduce K-or operation
by extending the standard bitwise OR. In K-or, a bit position in the result is set to 1 if at least
k numbers in nums have a 1 in that position.
Return the K-or of nums.r"""

from typing import List


class Solution:
    @staticmethod
    def findKOr(nums: List[int], k: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        or_result = 0

        # Iterate through each bit position from least significant bit to most significant bit
        for i in range(32):
            # Count the number of 1s in the ith bit position
            count = 0
            for num in nums:
                count += (num >> i) & 1

            # If the count is greater than or equal to k, set the ith bit position to 1
            if count >= k:
                or_result |= 1 << i

        return or_result


# Unit Test: nums = [7,12,9,8,9,15], k = 4, Output: 9
assert Solution.findKOr([7, 12, 9, 8, 9, 15], 4) == 9

# Unit Test: nums = [2,12,1,11,4,5], k = 6, Output: 0
assert Solution.findKOr([2, 12, 1, 11, 4, 5], 6) == 0

# Unit Test: nums = [10,8,5,9,11,6,8], k = 1, Output: 15
assert Solution.findKOr([10, 8, 5, 9, 11, 6, 8], 1) == 15

print("All unit tests are passed.")

"""1018. Binary Prefix Divisible By 5
Link: https://leetcode.com/problems/binary-prefix-divisible-by-5
Difficulty: Easy
Description: You are given a binary array nums (0-indexed).
We define xi as the number whose binary representation is the subarray nums[0..i]
(from most-significant bit to least-significant bit).
For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5."""

from typing import List


class Solution:
    @staticmethod
    def prefixesDivBy5(nums: List[int]) -> List[bool]:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the prefix sum and the result
        prefix_sum, result = 0, []

        # Iterate through the binary array
        for num in nums:
            # prefix_sum * 2 is equivalent to (prefix_sum << 1), % 5 here because:
            # 1. Check if the prefix sum is divisible by 5 without growing too large;
            # 2. We don't care about the actual value, just the remainder:
            # E.g. 11 % 5 = 1 % 5 -> 22 % 5 = 2 % 5 -> 44 % 5 = 4 % 5
            prefix_sum = (prefix_sum * 2 + num) % 5

            result.append(prefix_sum == 0)

        return result


# Unit Test: nums = [1, 0, 1], Output: [False, False, True]
assert Solution.prefixesDivBy5([1, 0, 1]) == [False, False, True]

# Unit Test: nums = [0, 1, 1], Output: [True, False, False]
assert Solution.prefixesDivBy5([0, 1, 1]) == [True, False, False]

# Unit Test: nums = [1, 1, 1], Output: [False, False, False]
assert Solution.prefixesDivBy5([1, 1, 1]) == [False, False, False]

# Unit Test: nums = [0, 1, 1, 1, 1, 1], Output: [True, False, False, False, True, False]
assert Solution.prefixesDivBy5([0, 1, 1, 1, 1, 1]) == [True, False, False, False, True, False]

print("All unit tests are passed")

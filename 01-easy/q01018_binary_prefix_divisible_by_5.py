"""1018. Binary Prefix Divisible By 5
Link: https://leetcode.com/problems/binary-prefix-divisible-by-5
Difficulty: Easy
Description: You are given a binary array nums (0-indexed).
We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).
• For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5."""

from typing import List


class Solution:
    @staticmethod
    def prefixesDivBy5(nums: List[int]) -> List[bool]:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1)."""
        prefix_sum, result = 0, []

        # Iterate through the binary array
        for num in nums:
            prefix_sum = (prefix_sum * 2 + num)
            result.append(prefix_sum % 5 == 0)

        return result


def unit_tests():
    # Input: nums = [1, 0, 1], Output: [False, False, True]
    assert Solution.prefixesDivBy5([1, 0, 1]) == [False, False, True]

    # Input: nums = [0, 1, 1], Output: [True, False, False]
    assert Solution.prefixesDivBy5([0, 1, 1]) == [True, False, False]

    # Input: nums = [1, 1, 1], Output: [False, False, False]
    assert Solution.prefixesDivBy5([1, 1, 1]) == [False, False, False]

    # Input: nums = [0, 1, 1, 1, 1, 1], Output: [True, False, False, False, True, False]
    assert Solution.prefixesDivBy5([0, 1, 1, 1, 1, 1]) == [True, False, False, False, True, False]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

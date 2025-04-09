"""2932. Maximum Strong Pair XOR I
Link: https://leetcode.com/problems/maximum-strong-pair-xor-i/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums. A pair of integers x and y is called a
strong pair if it satisfies the condition:
- |x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and their bitwise
XOR is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair."""

from typing import List


class Solution:
    @staticmethod
    def maximumStrongPairXor(nums: List[int]) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(n), Space Complexity: O(1)."""
        max_xor = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    max_xor = max(max_xor, nums[i] ^ nums[j])

        return max_xor


# Unit Test: nums = [1,2,3,4,5], Output: 7
assert Solution.maximumStrongPairXor([1, 2, 3, 4, 5]) == 7

# Unit Test: nums = [10,100], Output: 0
assert Solution.maximumStrongPairXor([10, 100]) == 0

# Unit Test: nums = [5,6,25,30], Output: 7
assert Solution.maximumStrongPairXor([5, 6, 25, 30]) == 7

print("All unit tests are passed.")

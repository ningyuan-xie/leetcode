"""2859. Sum of Values at Indices With K Set Bits
Link: https://leetcode.com/problems/sum-of-values-at-indices-with-k-bits/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums and an integer k.
Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly
k set bits in their binary representation.
The set bits in an integer are the 1's present when it is written in binary.
- For example, the binary representation of 21 is 10101, which has 3 set bits.m"""

from typing import List


class Solution:
    @staticmethod
    def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the sum of elements with k set bits
        sum_elements = 0

        def countSetBits(num: int) -> int:
            """Helper function to count the number of set bits in a number"""
            count = 0
            while num:
                count += num & 1
                num >>= 1  # num is right shifted by 1 bit, removing the rightmost bit
            return count

        # Calculate the sum of elements with k set bits
        for i in range(len(nums)):
            if countSetBits(i) == k:
                sum_elements += nums[i]
        return sum_elements


# Input: nums = [5,10,1,5,2], k = 1, Output: 13
assert Solution.sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1) == 13

# Input: nums = [4,3,2,1], k = 2, Output: 1
assert Solution.sumIndicesWithKSetBits([4, 3, 2, 1], 2) == 1

print("All unit tests are passed.")

"""3467. Transform Array by Parity
Link: https://leetcode.com/problems/transform-array-by-parity/
Difficulty: Easy
Description: You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:
1. Replace each even number with 0.
2. Replace each odd numbers with 1.
3. Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations."""

from typing import List


class Solution:
    @staticmethod
    def transformArray(nums: List[int]) -> List[int]:
        """Optimal Solution: List Comprehension and Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(n)."""
        # Replace even numbers with 0 and odd numbers with 1
        transformed = [0 if num % 2 == 0 else 1 for num in nums]
        
        # Sort the modified array
        transformed.sort()
        
        return transformed


def unit_tests():
    # Input: nums = [4,3,2,1], Output: [0,0,1,1]
    assert Solution.transformArray([4, 3, 2, 1]) == [0, 0, 1, 1]

    # Input: nums = [1,5,1,4,2], Output: [0,0,1,1,1]
    assert Solution.transformArray([1, 5, 1, 4, 2]) == [0, 0, 1, 1, 1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")

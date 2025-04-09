"""2455. Average Value of Even Numbers That Are Divisible by Three
Link: https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
Difficulty: Easy
Description: Given an integer array nums of positive integers, return the average value of all even
integers that are divisible by 3.
Note that the average of n elements is the sum of the n elements divided by n and rounded down to the
nearest integer."""

from typing import List


class Solution:
    @staticmethod
    def averageValue(nums: List[int]) -> int:
        """Optimal Solution: Array. Time Complexity: O(n), Space Complexity: O(1)."""
        current_sum = 0
        count = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                current_sum += num
                count += 1
        return current_sum // count if count > 0 else 0


# Unit Test: nums = [1,3,6,10,12,15], Output: 9
assert Solution.averageValue([1, 3, 6, 10, 12, 15]) == 9

# Unit Test: nums = [1,2,4,7,10], Output: 0
assert Solution.averageValue([1, 2, 4, 7, 10]) == 0

print("All unit tests are passed.")

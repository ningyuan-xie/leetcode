"""1295. Find Numbers with Even Number of Digits
Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Difficulty: Easy
Description: Given an array nums of integers, return how many of them contain an even number of
digits."""

from typing import List


class Solution:
    @staticmethod
    def findNumbers(nums: List[int]) -> int:
        """Optimal Solution: Counting Digits. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the count
        count = 0

        # Traverse the array
        for num in nums:
            # Count the number of digits
            num_digits = 0
            while num:
                num //= 10
                num_digits += 1

            # Increment the count if the number of digits is even
            if num_digits % 2 == 0:
                count += 1

        return count


# Unit Test: nums = [12, 345, 2, 6, 7896], Output: 2
assert Solution.findNumbers([12, 345, 2, 6, 7896]) == 2

# Unit Test: nums = [555, 901, 482, 1771], Output: 1
assert Solution.findNumbers([555, 901, 482, 1771]) == 1

print("All unit tests are passed.")

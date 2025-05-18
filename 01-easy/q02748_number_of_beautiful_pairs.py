"""2748. Number of Beautiful Pairs
Link: https://leetcode.com/problems/number-of-beautiful-pairs/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j <
nums.length is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.
Return the total number of beautiful pairs in nums.
Two integers x and y are coprime if there is no integer greater than 1 that divides both of them.
In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor
of x and y."""

from typing import List


class Solution:
    @staticmethod
    def countBeautifulPairs(nums: List[int]) -> int:
        """Optimal Solution: GCD. Time Complexity: O(n^2), Space Complexity: O(1)."""
        # Initialize the count
        count = 0
        n = len(nums)

        def gcd(a: int, b: int) -> int:
            """Helper function to calculate the greatest common divisor"""
            while b:
                a, b = b, a % b
            return a

        # Check each pair of numbers
        for i in range(n - 1):
            for j in range(i + 1, n):
                first_num = int(str(nums[i])[0])
                second_num = int(str(nums[j])[-1])

                if gcd(first_num, second_num) == 1:
                    count += 1
        return count


# Unit Test: nums = [2,5,1,4], Output: 5
assert Solution.countBeautifulPairs([2, 5, 1, 4]) == 5

# Unit Test: nums = [11,21,12], Output: 2
assert Solution.countBeautifulPairs([11, 21, 12]) == 2

print("All unit tests are passed.")
